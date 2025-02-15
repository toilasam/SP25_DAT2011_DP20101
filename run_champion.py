import os, importlib

def dynamic_import(champion_folder, champion_file):
    module_name = champion_folder + '.' + champion_file
    module_name = module_name.replace('.py', '')
    module = importlib.import_module(module_name)

    class_name = champion_file.replace('.py','')
    cls = getattr(module, class_name)

    champion = cls()
    return champion

champion_folder = 'champions'

champion_files = os.listdir(champion_folder)

for champion_file in champion_files:
    if not champion_file.endswith('.py'):
        continue
    champion = dynamic_import(champion_folder, champion_file)
    champion.attack()