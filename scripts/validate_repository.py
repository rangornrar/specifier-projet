#!/usr/bin/env python3
"""Contrôles statiques du dépôt ; ne remplace pas une recette du comportement."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.venv', 'venv', '__pycache__', 'output', 'outputs', 'tmp'}
ERRORS = []


def error(message):
    ERRORS.append(message)


def local_file(source, target):
    """Résoudre un chemin relatif en restant dans le dépôt."""
    path = (source.parent / unquote(target)).resolve()
    if not path.is_relative_to(ROOT):
        error(f'{source.relative_to(ROOT)} : chemin hors du dépôt : {target}')
    elif not path.exists():
        error(f'{source.relative_to(ROOT)} : cible absente : {target}')


def load_mapping(path):
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            raise ValueError('un objet YAML est attendu')
        return data
    except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
        error(f'{path.relative_to(ROOT)} : {exc}')
        return {}


def check_skill():
    path = ROOT / 'SKILL.md'
    try:
        text = path.read_text(encoding='utf-8')
        match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
        if not match:
            raise ValueError('frontmatter YAML absent ou incomplet')
        data = yaml.safe_load(match.group(1))
        if not isinstance(data, dict):
            raise ValueError('le frontmatter doit être un objet YAML')
        if data.get('name') != 'specifier-projet':
            error('SKILL.md : le nom attendu est specifier-projet')
        description = data.get('description')
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            error('SKILL.md : description non vide de 1024 caractères maximum attendue')
        if not text[match.end():].strip():
            error('SKILL.md : instructions absentes')
    except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
        error(f'SKILL.md : {exc}')


def check_interface(data):
    interface = data.get('interface')
    if not isinstance(interface, dict):
        error('agents/openai.yaml : interface absente')
        return
    for key in ('display_name', 'short_description', 'default_prompt'):
        if not isinstance(interface.get(key), str) or not interface[key].strip():
            error(f'agents/openai.yaml : {key} absent ou vide')
    for key in ('icon_small', 'icon_large'):
        target = interface.get(key)
        if not isinstance(target, str) or not target.strip():
            error(f'agents/openai.yaml : {key} absent ou vide')
        else:
            # Les icônes sont relatives à la racine du skill.
            local_file(ROOT / 'SKILL.md', target)
    policy = data.get('policy', {})
    if not isinstance(policy, dict):
        error('agents/openai.yaml : policy doit être un objet')
    elif 'allow_implicit_invocation' in policy and not isinstance(policy['allow_implicit_invocation'], bool):
        error('agents/openai.yaml : allow_implicit_invocation doit être booléen')


def check_markdown(path):
    text = path.read_text(encoding='utf-8')
    # Ne pas interpréter les exemples de commandes comme des liens.
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    # Liens inline et définitions de références ; ancres et URL externes ignorées.
    body = '\n'.join(lines)
    targets = re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)', body)
    targets += re.findall(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', body, re.M)
    for target in targets:
        target = target.strip('<>')
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        local_file(path, parsed.path)


def main():
    required = (
        'SKILL.md', 'agents/openai.yaml', 'assets/icon.svg',
        'references/domaines.md', 'references/plan-dossier.md',
        'README.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
        'docs/UTILISATION.md', 'docs/VALIDATION.md', 'examples/DEMANDES.md',
    )
    for name in required:
        if not (ROOT / name).is_file():
            error(f'Fichier requis absent : {name}')
    check_skill()
    files = [p for p in ROOT.rglob('*') if p.is_file() and not set(p.relative_to(ROOT).parts) & EXCLUDED]
    for path in files:
        if path.suffix in ('.yml', '.yaml'):
            data = load_mapping(path)
            if path == ROOT / 'agents/openai.yaml':
                check_interface(data)
        elif path.suffix == '.md':
            try:
                check_markdown(path)
            except (OSError, UnicodeError, ValueError) as exc:
                error(f'{path.relative_to(ROOT)} : {exc}')
    try:
        if ET.parse(ROOT / 'assets/icon.svg').getroot().tag != '{http://www.w3.org/2000/svg}svg':
            error('assets/icon.svg : élément racine SVG attendu')
    except (OSError, ET.ParseError) as exc:
        error(f'assets/icon.svg : {exc}')
    if ERRORS:
        print('\n'.join(f'ERREUR : {message}' for message in ERRORS))
        return 1
    print(f'Validation réussie : {len(files)} fichiers, métadonnées et liens locaux vérifiés.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
