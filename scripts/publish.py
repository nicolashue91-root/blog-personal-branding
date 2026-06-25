import os
import shutil

# Définition des chemins absolus sur la machine Windows de l'hôte
SOURCE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "content_pipeline", "published", "pillar_content", "blog"
    )
)
TARGET_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "src",
        "content",
        "blog"
    )
)

def has_yaml_frontmatter(filepath):
    """Vérifie si le fichier commence par un bloc de frontmatter YAML (débutant par ---)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            return first_line == "---"
    except Exception as e:
        print(f"[Warning] Impossible de lire {filepath} pour vérifier le frontmatter : {e}")
        return False

def import_articles():
    print(f"[Import] Recherche d'articles dans la source : {SOURCE_DIR}")
    print(f"[Import] Répertoire de destination du blog : {TARGET_DIR}")

    if not os.path.exists(SOURCE_DIR):
        print(f"[Error] Le répertoire source est introuvable.")
        return

    # Nettoyage préalable des anciens fichiers importés pour éviter des résidus non valides
    if os.path.exists(TARGET_DIR):
        for file in os.listdir(TARGET_DIR):
            file_path = os.path.join(TARGET_DIR, file)
            # On ne supprime pas l'article de test ia-agentique-qse.mdx s'il n'est pas dans la source
            if os.path.isfile(file_path) and file != "ia-agentique-qse.mdx":
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"[Warning] Impossible de nettoyer {file} : {e}")

    if not os.path.exists(TARGET_DIR):
        try:
            os.makedirs(TARGET_DIR, exist_ok=True)
        except Exception as e:
            print(f"[Error] Impossible de créer le répertoire destination : {e}")
            return

    copied_count = 0
    ignored_count = 0
    
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".md") or filename.endswith(".mdx"):
            source_path = os.path.join(SOURCE_DIR, filename)
            
            # Filtrage strict : importer uniquement si le fichier a un frontmatter valide
            if has_yaml_frontmatter(source_path):
                target_path = os.path.join(TARGET_DIR, filename)
                try:
                    shutil.copy2(source_path, target_path)
                    print(f"[Import] Copié (Valide Frontmatter) : {filename}")
                    copied_count += 1
                except Exception as e:
                    print(f"[Error] Échec de l'import de {filename} : {e}")
            else:
                ignored_count += 1

    print(f"[Import] Opération terminée.")
    print(f" -> {copied_count} article(s) importé(s) avec succès.")
    print(f" -> {ignored_count} fichier(s) ignoré(s) (absence de frontmatter YAML).")

if __name__ == "__main__":
    import_articles()
