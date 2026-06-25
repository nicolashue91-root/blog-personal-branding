# Blog Technique — Architecte de Systèmes QSE Autonomes

Blog statique minimaliste et ultra-performant propulsé par Astro, conçu pour publier des articles de fond sur la convergence entre l'IA agentique et la conformité ISO.

## 🚀 Fonctionnalités
- **Performance Instantanée** : Génération de site statique (SSG) sans JavaScript inutile côté client (zéro-JS footprint par défaut).
- **Design System Custom** : Vanilla CSS pur avec variables CSS (clair/sombre automatique basé sur le système, persistance manuelle via `localStorage`).
- **Contrat Frontmatter Strict** : Validation automatique du schéma des métadonnées (Zod) à chaque compilation.
- **Snacks Preview intégré** : Rendu en bas de page des déclinaisons de contenu générées pour LinkedIn et X par le Personal Branding Pipeline.

## 🛠️ Stack Technique
- **Framework** : Astro (SSG)
- **Rendu Contenu** : MDX
- **Style** : Vanilla CSS
- **Déploiement** : Cloudflare Pages (Edge)

## 💻 Développement Local

### Prérequis
- Node.js (v18.x ou supérieure)
- npm

### Installation
```bash
npm install
```

### Lancer le serveur de développement
```bash
npm run dev
```
Le serveur sera disponible sur `http://localhost:4321/`.

### Compiler pour la production
```bash
npm run build
```
Les fichiers statiques seront générés dans le dossier `/dist/`.

---

## 🤖 Intégration Personal Branding Pipeline

Les articles de blog sont rédigés de manière autonome par vos agents au sein du pipeline.

Pour importer automatiquement les articles validés depuis le dossier `published` du pipeline vers ce blog (si la copie automatique échoue), exécutez simplement la commande suivante à la racine du blog :

```bash
npm run import-posts
```

Ce script exécutera le programme Python `scripts/publish.py` qui récupérera les fichiers `.md` ou `.mdx` directement depuis le répertoire source (`../content_pipeline/published/pillar_content/blog`) et les copiera dans `src/content/blog/`.


---

## ☁️ Déploiement Cloudflare Pages

Le déploiement est automatisé via GitHub Actions à chaque push sur la branche `main`.

### Secrets GitHub à configurer :
1. `CLOUDFLARE_API_TOKEN` : Jeton d'API Cloudflare avec les permissions "Cloudflare Pages: Edit".
2. `CLOUDFLARE_ACCOUNT_ID` : Identifiant de votre compte Cloudflare.
