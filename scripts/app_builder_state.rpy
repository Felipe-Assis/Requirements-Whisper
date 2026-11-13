default campaign_layouts = {}
default campaign_builder_selected = "balance"
default campaign_builder_feedback = "Escolha um módulo e uma posição, ou arraste o cartão."

init python:
    CAMPAIGN_MODULES = {"balance": "Total do mês", "records": "Lançamentos", "actions": "Ações e recuperação"}

    def campaign_layout(project_id):
        return list(store.campaign_layouts.get(project_id, ["balance", "records", "actions"]))

    def campaign_place_module(project_id, module, slot):
        layout = campaign_layout(project_id)
        if module not in layout or type(slot) is not int or slot not in range(3):
            return False
        old_slot = layout.index(module)
        layout[old_slot], layout[slot] = layout[slot], layout[old_slot]
        store.campaign_layouts = dict(store.campaign_layouts, **{project_id: layout})
        store.campaign_builder_feedback = CAMPAIGN_MODULES[module] + " na posição " + str(slot + 1) + ". Essa ordem será usada no aplicativo."
        return True

