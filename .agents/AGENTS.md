# Règles de projet — Blog Nicolas Hue

Ce fichier définit les consignes de qualité, de structure et de déploiement à appliquer systématiquement lors de toute contribution à ce projet.

## 1. Référentiel Éditorial & Style
*   **Règle absolue** : Ne **jamais** utiliser le tiret cadratin (`—`) dans les textes rédigés en français. Utiliser des virgules, des parenthèses, ou un tiret court (`-`).
*   **Langue** : Tous les contenus publics (articles, en-têtes, navigation, pieds de page) doivent être rédigés en français professionnel, fluide et orienté action.
*   **Persona cible** : Le contenu s'adresse à des professionnels du QSE et de la gestion des risques (comme Marc). Le ton doit être didactique, technique et sans artifice ("zero-fluff"). Éviter d'appeler explicitement le prénom "Marc" dans les textes publics.

## 2. Métadonnées & SEO des Articles
Chaque nouvel article (`src/content/blog/*.mdx` ou `*.md`) doit respecter le schéma de métadonnées suivant :
*   **Titre (`title`)** : Doit être explicite, contenir des mots-clés cibles, et ne pas dépasser **60 caractères** dans la mesure du possible.
*   **Description (`description`)** : Résumé d'accroche pour les moteurs de recherche de **120 à 160 caractères**.
*   **Slug (Nom de fichier et d'URL)** : Doit être uniquement composé de lettres minuscules, chiffres et tirets courts (`-`), sans caractères accentués ou spéciaux.
*   **Catégorie (`pilier`)** : Doit classer l'article dans l'un des piliers méthodologiques du blog (ex: `Convergence`, `IA Agentique`, `Technique`).
*   **Date (`date`)** : Date de publication au format ISO (`YYYY-MM-DD`).

## 3. Gestion des Médias
*   Les images propres à un article doivent être stockées dans un dossier structuré comme suit : `public/images/<article-slug>/`.
*   Toutes les images déclarées en Markdown ou HTML doivent obligatoirement posséder un attribut de texte alternatif (`alt`) descriptif pour l'accessibilité et le SEO.

## 4. Protocole de Validation et de Livraison
Après chaque ajout ou modification d'article ou de code, l'agent doit exécuter la séquence suivante :
1.  **Vérification de compilation** : Lancer `npm run build` en local pour vérifier qu'aucune erreur MDX ou Astro ne bloque le build.
2.  **Sitemap & Redirections** : S'assurer que le fichier `dist/sitemap-index.xml` et les redirections sont correctement générés.
3.  **Livraison Git** :
    *   Indexer les sources et le dossier `/dist` compilé : `git add .` (en excluant node_modules).
    *   Créer un commit clair (ex: `feat(blog): publier l'article sur <sujet>`).
    *   Pousser sur la branche principale : `git push` pour déclencher le déploiement sur Cloudflare Pages.
