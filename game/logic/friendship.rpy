#amizade.rpy
# Variáveis de amizade, uma para cada personagem principal (começam do zero)
default amizade_developer_test = 0.0
default amizade_developer_coding = 0.0
default amizade_developer_management = 0.0
default amizade_developer_requirements = 0.0
default amizade_developer_ai = 0.0
default amizade_developer_quality = 0.0
default amizade_developer_project = 0.0
default amizade_developer_security = 0.0

default amizade_doutora_1 = 0.0
default amizade_doutora_2 = 0.0


init python:
    def add_contact(contact_id):
        # store.contacts é garantido pelo `default contacts = set()` em state_flags.rpy
        # Adiciona ao set, se ainda não estiver
        if contact_id not in store.contacts:
            store.contacts.add(contact_id)
            # Tenta setar a variável booleana global correspondente (ex: contato_developer_ai)
            var_name = "contato_" + contact_id
            if hasattr(store, var_name):
                setattr(store, var_name, True)
            # Notifica nome amigável, se possível
            try:
                nome = AMIGOS_DATA[contact_id]["name"]
                renpy.notify(_("Contato adicionado: {nome}").format(nome=nome))
            except:
                renpy.notify(_("Contato adicionado: {nome}").format(nome=contact_id.replace('_',' ').capitalize()))
        else:
            renpy.notify(_("Contato já adicionado."))


    def add_friendship_point(character_id, amount=0.5):
        """
        Adiciona pontos de amizade ao personagem e notifica o jogador.
        O valor resultante é mantido no intervalo 0..10 (clamp).
        Exemplo: $ add_friendship_point("developer_requirements")
        """
        var_name = "amizade_" + character_id
        if hasattr(store, var_name):
            current = getattr(store, var_name)
            new_value = min(max(current + amount, 0), 10)
            setattr(store, var_name, new_value)
            # Notificação: tenta usar nome bonito se existir em AMIGOS_DATA
            try:
                nome = AMIGOS_DATA[character_id]["name"]
                renpy.notify(_("Pontos de amizade com {nome} +{amount} (Total: {new_value})").format(nome=nome, amount=amount, new_value=new_value))
            except:
                renpy.notify(_("Pontos de amizade com {nome} +{amount} (Total: {new_value})").format(nome=character_id.replace('_',' ').capitalize(), amount=amount, new_value=new_value))
            # Debug opcional no log
            renpy.log(f"Pontos de amizade de {var_name}: {new_value}")
        else:
            renpy.log(f"Personagem não encontrado: {var_name}")

    def get_friendship_point(character_id):
        """
        Retorna os pontos de amizade do personagem.
        """
        var_name = "amizade_" + character_id
        if hasattr(store, var_name):
            return getattr(store, var_name)
        else:
            renpy.log(f"Personagem não encontrado: {var_name}")
            return 0

    def friendship_color(level):
        """
        Cor da barra de amizade (escada única de 5 limiares, usando >=).
        Será ligada à UI de contatos numa fase posterior.
        """
        if level >= 10:
            return "#44D067"
        elif level >= 8:
            return "#A4EB9E"
        elif level >= 5:
            return "#FFEB3B"
        elif level >= 3:
            return "#FFA149"
        else:
            return "#FF5353"
