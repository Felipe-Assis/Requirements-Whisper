# inventory.rpy
# Mutador de inventário no store global (sem UI).
# A UI da Mochila fica em ui/inventory_screen.rpy (mechanics/).

init python:
    def add_to_inventory(item_name):
        var_name = f"item_{item_name}"
        if hasattr(store, var_name):
            setattr(store, var_name, True)
            renpy.notify(_("Item adicionado ao inventário: {item}").format(item=item_name.replace('_',' ').capitalize()))
        else:
            renpy.notify(_("Item não reconhecido."))
