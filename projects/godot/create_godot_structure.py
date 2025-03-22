import os

def create_godot_project_structure(project_path):
    """Creates the recommended Godot project folder structure."""

    folders = [
        os.path.join(project_path, "addons"),
        os.path.join(project_path, "assets", "animations"),
        os.path.join(project_path, "assets", "audio", "music"),
        os.path.join(project_path, "assets", "audio", "sfx"),
        os.path.join(project_path, "assets", "fonts"),
        os.path.join(project_path, "assets", "images", "characters"),
        os.path.join(project_path, "assets", "images", "environment"),
        os.path.join(project_path, "assets", "images", "ui"),
        os.path.join(project_path, "assets", "images", "tilesets"),
        os.path.join(project_path, "assets", "materials"),
        os.path.join(project_path, "assets", "meshes"),
        os.path.join(project_path, "assets", "scenes"),
        os.path.join(project_path, "assets", "shaders"),
        os.path.join(project_path, "assets", "textures"),
        os.path.join(project_path, "assets", "ui"),
        os.path.join(project_path, "scripts", "characters"),
        os.path.join(project_path, "scripts", "gameplay"),
        os.path.join(project_path, "scripts", "ui"),
        os.path.join(project_path, "scripts", "utilities"),
        os.path.join(project_path, "scenes", "levels"),
        os.path.join(project_path, "scenes", "objects"),
        os.path.join(project_path, "scenes", "ui"),
        os.path.join(project_path, "scenes", "prefabs"),
        os.path.join(project_path, "autoload")
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    project_path = os.path.join(os.getcwd(), project_name)
    create_godot_project_structure(project_path)
    print(f"Godot project structure created at: {project_path}")