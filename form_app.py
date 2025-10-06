
import streamlit as st

FORM_TITLE = "Лид-менеджмент (LM): Предоставление доступа"
TRIGGER_CHANNEL = "Укажите канал для доступа:"
TRIGGER_ROLE = "Укажите роль:"

channels = [
    "ГАП","ГПО","НПС","НДС","ГПХ","ИТМ","B2G","Средний сегмент",
    "ОКН","3К","ПДЗ и Ликвидированные","Процесс ликвидации/реорганизации",
    "Нестандартная роль (подробно опишу в поле дополнительная информация)",
]

channel_descriptions = {
    "ГАП": "Группа активных продаж, целью которой является продажа услуг Ростелекома. Сотрудники оформляются в штат.",
    "ГПО": "Группа продаж и обслуживания, целью которой является работа с действующими клиентами Ростелекома (продажа новых продуктов, допродажа доп. услуг по подключенным продуктам, решение проблем клиента)",
    "НПС": "Группа по работе с лояльностью клиентов, целью которой является выявление причины оттока и удержание клиентов, например, путём предоставления скидок на услуги Ростелекома или помощь в решении текущих проблем",
    "НДС": "Группа НДС – это Направление по дистанционному сервису, работают в Управлении по дистанционному сервису и развитию клиентского портфеля.",
    "ГПХ": "Группа активных продаж, целью которой является продажа услуг Ростелекома. Сотрудники оформляются по договору (трудоустройство по ГПХ не является причиной выбора канала ГПХ, необходимо выбирать канал в соответствии с группой сотрудников, с которой предстоит работать) ",
    "ИТМ": "Группа исходящего телемаркетинга. В этом канале работает НОД – направление обработки дистанции – подразделение продаж, ответственное за обработку лидов от клиентов, обратившихся по дистанционным каналам: сайт RT.RU, звонок в контакт-центр ПАО Ростелеком, ЛК ЮЛ и пр.",
    "B2G": "Группа по работе с позициями ПГ",
    "Средний сегмент": "Раздел для сотрудников канала ГПО, предназначенный для работы с клиентами среднего сегмента, взаимодействие с которыми происходит на протяжении длительного периода времени, включает в себя ведение и дополнение карточки клиента, и осуществление продаж. Для предоставления данной роли так же заводится доступ в канале ГПО.",
    "ОКН": "Раздел для сотрудников канала ОКНН, предназначенный для работы с объектами коммерческой недвижимости",
    "3К": "В этом канале работает 3К – Крупные Корпоративные Клиенты – подразделение продаж, ответственное за обработку лидов данного сегмента",
    "ПДЗ и Ликвидированные": "Группа по работе с просроченной дебиторской задолженностью, реорганизацией и ликвидированными компаниями. Для предоставления данной роли так же заводится доступ в канале ГПО.",
    "Процесс ликвидации/реорганизации": "Группа по работе с компаниями, которые находятся в процессе ликвидации/реорганизации. С такими Клиентами необходимо перезаключить договор или присвоить Клиенту статус «Ликвидирован». Для предоставления данной роли так же заводится доступ в канале ГПО.",
    "Нестандартная роль (подробно опишу в поле дополнительная информация)": "Группа по работе с просроченной дебиторской задолженностью, реорганизацией и ликвидированными компаниями. Для предоставления данной роли так же заводится доступ в канале ГПО.",
}

roles_general = ["Исполнитель","Групп-лидер","Руководитель канала","Руководитель РФ","Руководитель каналов РД","Руководитель каналов КЦ"]
role_texts_general = {
    "Исполнитель": "Данная роль предназначена для менеджеров, которые непосредственно работают с назначенными на них лидами, клиентами и позициями ПГ.  Исполнитель может работать только в одном канале.",
    "Групп-лидер": "Данная роль предназначена для руководителей групп, которые назначают лиды  на менеджеров, работают с отчетностью по своим группам, а так же могут сами отрабатывать задания. Групп-лидер может работать только в одном канале",
    "Руководитель канала": "Данная роль предназначена для региональных руководителей каналов, которые назначают лиды  на руководителей групп и менеджеров, работают с отчетностью, а так же могут сами отрабатывать задания. Руководителю канала может быть доступно несколько каналов",
    "Руководитель РФ": "Данная роль не предусматривает возможности производить назначение лидов и самостоятельную отработку. Роль предназначена для региональных руководителей, которые работают с отчетностью.  Руководителю РФ по умолчанию доступна статистика по всем каналам. Учетная запись может быть заведена только на уровне РФ.",
    "Руководитель каналов РД": "Данная роль не предусматривает возможности производить назначение лидов и самостоятельную отработку. Роль предназначена для руководителей на уровне РД, которые работают с отчетностью. Руководителю РД в профиле может быть доступно несколько каналов и несколько РД",
    "Руководитель каналов КЦ": "Данная роль не предусматривает возможности производить назначение лидов и самостоятельную отработку. Роль предназначена для руководителей на уровне КЦ, которые работают с отчетностью. Руководителю КЦ в профиле может быть доступно несколько каналов",
}

roles_okn = ["Исполнитель","Менеджер сопровождения ОКН","Руководитель канала","Руководитель каналов РД","Руководитель каналов КЦ"]
role_texts_okn = {
    "Исполнитель": "Данная роль предназначена для менеджеров, которые непосредственно работают с назначенными на них объектами ОКН.",
    "Менеджер сопровождения ОКН": "Данная роль предназначена для сотрудников, которые ведут сопровождение финансово-экономической деятельности ОКН. Пользователь, который имеет доступ к ОКН, где он закреплен как менеджер сопровождения может редактировать все поля в карточке ОКН, статус объекта и переназначать Исполнителя",
    "Руководитель канала": "Данная роль предназначена для региональных руководителей каналов, которые назначают объекты ОКН на менеджеров, работают с отчетностью, а так же могут сами отрабатывать задания.",
    "Руководитель каналов РД": "Данная роль не предусматривает возможности производить назначение объектов ОКН и самостоятельную отработку. Роль предназначена для руководителей, которые работают с отчетностью.",
    "Руководитель каналов КЦ": "Данная роль не предусматривает возможности производить назначение объектов ОКН и самостоятельную отработку. Роль предназначена для руководителей на уровне КЦ, которые работают с отчетностью.",
}

roles_with_extra_general = {"Руководитель канала","Руководитель РФ","Руководитель каналов РД","Руководитель каналов КЦ"}
roles_with_extra_okn = {"Руководитель каналов КЦ"}
extra_channel_options = ["ГАП","ГПО","НПС","НДС","ГПХ","ИТМ","B2G","Средний сегмент","ПДЗ и Ликвидированные","Процесс ликвидации/реорганизации"]

RD_LIST = ["РД Центр","РД Северо-Запад","РД Волга","РД Юг","РД Урал","РД Сибирь","РД Дальний Восток","РД Москва и Московская область"]
RF_BRANCHES = ["Белгородский филиал","Брянский филиал","Воронежский филиал","Калужский филиал","Магаданский филиал","Камчатский филиал","Амурский филиал","Сахалинский филиал","Хабаровский филиал","Филиал Сахателеком","Московский филиал"]

CHANNELS_DIRECT_RD = {"ИТМ","3К","ОКН","НДС","НПС"}

st.set_page_config(page_title=FORM_TITLE, page_icon="🧩", layout="centered")
st.title(FORM_TITLE)

# State
if "extra_channels" not in st.session_state: st.session_state.extra_channels = []
if "prev_role" not in st.session_state: st.session_state.prev_role = None
if "prev_channel" not in st.session_state: st.session_state.prev_channel = None
if "extra_rd" not in st.session_state: st.session_state.extra_rd = []   # stores list of selected extra RD values (or None)
if "level_select" not in st.session_state: st.session_state.level_select = None

# Channel
channel = st.selectbox(TRIGGER_CHANNEL, channels, index=None, placeholder="Выберите канал", key="main_channel")

# Reset on change
if channel != st.session_state.prev_channel:
    st.session_state.prev_channel = channel
    st.session_state.extra_channels = []
    st.session_state.extra_rd = []
    st.session_state.role_select = None
    st.session_state.level_select = None
    for k in ["gpo_mid","gpo_pdz","gpo_proc"]:
        st.session_state[k] = False

# Description
if channel:
    desc = channel_descriptions.get(channel)
    if desc: st.info(desc)

# GPO extras
if channel == "ГПО":
    st.write("Для острудников ГПО дополнительные каналы:")
    c1,c2,c3 = st.columns(3)
    with c1: st.checkbox("Средний сегмент", key="gpo_mid")
    with c2: st.checkbox("ПДЗ и Ликвидированные", key="gpo_pdz")
    with c3: st.checkbox("Процесс ликвидации/реорганизации", key="gpo_proc")

# Roles
selected_role = None
roles_list = []
role_texts_map = {}
roles_with_extra = set()

if channel:
    if channel == "ОКН":
        roles_list = roles_okn; role_texts_map = role_texts_okn; roles_with_extra = roles_with_extra_okn
    elif channel == "Нестандартная роль (подробно опишу в поле дополнительная информация)":
        roles_list = []; role_texts_map = {}; roles_with_extra = set()
    else:
        roles_list = roles_general; role_texts_map = role_texts_general; roles_with_extra = roles_with_extra_general

    if roles_list:
        selected_role = st.selectbox(TRIGGER_ROLE, roles_list, index=None, placeholder="Выберите роль", key="role_select")

        if selected_role != st.session_state.prev_role:
            st.session_state.prev_role = selected_role
            st.session_state.extra_channels = []
            st.session_state.extra_rd = []

        if selected_role:
            st.markdown("**Описание роли**")
            st.write(role_texts_map[selected_role])

            if selected_role in roles_with_extra:
                if st.button("Добавить дополнительный канал"):
                    st.session_state.extra_channels.append(None)

                st.write("")
                to_remove = []
                for i,_ in enumerate(st.session_state.extra_channels):
                    st.markdown(f"**Дополнительный канал #{i+1}**")
                    sel_col, btn_col = st.columns([6,1], vertical_alignment="bottom")
                    with sel_col:
                        st.session_state.extra_channels[i] = st.selectbox(
                            "",
                            extra_channel_options,
                            index=None,
                            placeholder="Выберите канал",
                            key=f"extra_channel_{i}",
                            label_visibility="collapsed"
                        )
                    with btn_col:
                        st.write("")
                        if st.button("Удалить", key=f"del_extra_channel_{i}"):
                            to_remove.append(i)
                for idx in reversed(to_remove):
                    del st.session_state.extra_channels[idx]

# Region logic (hidden for 'Руководитель каналов КЦ')
hide_regions = (selected_role == "Руководитель каналов КЦ")

selected_rd = None; selected_level = None; selected_rf_branch = None

if not hide_regions and channel:
    if channel in CHANNELS_DIRECT_RD:
        selected_rd = st.selectbox("Укажите РД в котором необходимо создать УЗ:", RD_LIST, index=None, placeholder="Выберите РД", key="rd_direct")
    else:
        selected_level = st.selectbox("Учетную запись необходимо создать на уровне:", ["РФ (Региональный филиал)","РД (Региональная дирекция)"], index=None, placeholder="Выберите уровень", key="level_select")
        if selected_level == "РФ (Региональный филиал)":
            selected_rf_branch = st.selectbox("Выберите филиал РФ:", RF_BRANCHES, index=None, placeholder="Выберите филиал", key="rf_branch")
        elif selected_level == "РД (Региональная дирекция)":
            selected_rd = st.selectbox("Выберите РД:", RD_LIST, index=None, placeholder="Выберите РД", key="rd_level")
            # Add extra RD button for specific roles
            if selected_role in {"Руководитель канала","Руководитель РФ","Руководитель каналов РД"}:
                if st.button("Добавить дополнительный РД"):
                    st.session_state.extra_rd.append(None)
                st.write("")
                to_remove_rd = []
                for i,_ in enumerate(st.session_state.extra_rd):
                    st.markdown(f"**Дополнительный РД #{i+1}**")
                    sel_col, btn_col = st.columns([6,1], vertical_alignment="bottom")
                    with sel_col:
                        st.session_state.extra_rd[i] = st.selectbox(
                            "",
                            RD_LIST,
                            index=None,
                            placeholder="Выберите РД",
                            key=f"extra_rd_{i}",
                            label_visibility="collapsed"
                        )
                    with btn_col:
                        st.write("")
                        if st.button("Удалить", key=f"del_extra_rd_{i}"):
                            to_remove_rd.append(i)
                for idx in reversed(to_remove_rd):
                    del st.session_state.extra_rd[idx]

# Bottom fields
st.divider()
add_info_required = (channel == "Нестандартная роль (подробно опишу в поле дополнительная информация)")
add_info_label = "Дополнительная информация:" + (" *" if add_info_required else "")
add_info = st.text_area(add_info_label, height=140, key="extra_info")
contact_method = st.selectbox("Удобный способ взаимодейтсвия:", ["Мобильный телефон","Почта"], index=None, placeholder="Выберите способ", key="contact_method")

# Submit
st.divider()
if st.button("Отправить заявку"):
    errors = []
    if not channel: errors.append("Выберите канал")
    if channel and channel != "Нестандартная роль (подробно опишу в поле дополнительная информация)" and not selected_role:
        errors.append("Выберите роль")

    if not hide_regions and channel:
        if channel in CHANNELS_DIRECT_RD:
            if selected_rd is None: errors.append("Выберите РД")
        else:
            if not selected_level: errors.append("Выберите уровень (РФ/РД)")
            else:
                if selected_level.startswith("РФ") and not selected_rf_branch: errors.append("Выберите филиал РФ")
                if selected_level.startswith("РД") and selected_rd is None: errors.append("Выберите РД")

    if add_info_required and not (add_info or "").strip(): errors.append("Заполните поле «Дополнительная информация»")
    if not contact_method: errors.append("Выберите удобный способ взаимодействия")

    if errors:
        st.error("\n".join("• "+e for e in errors))
    else:
        payload = {
            "Канал": channel,
            "Роль": selected_role,
            "Доп. каналы (кнопка)": [c for c in st.session_state.extra_channels if c],
            "ГПО: доп. каналы (чекбоксы)": {
                "Средний сегмент": st.session_state.get("gpo_mid", False),
                "ПДЗ и Ликвидированные": st.session_state.get("gpo_pdz", False),
                "Процесс ликвидации/реорганизации": st.session_state.get("gpo_proc", False),
            } if channel == "ГПО" else None,
            "Региональный уровень": None if hide_regions else {
                "Тип выбора": ("РД прямой" if channel in CHANNELS_DIRECT_RD else selected_level),
                "РД (основной)": selected_rd,
                "Филиал РФ": selected_rf_branch,
                "Доп. РД": [r for r in st.session_state.extra_rd if r],
            },
            "Доп. информация": (add_info or "").strip(),
            "Контакт": contact_method,
        }
        st.success("Заявка отправлена (демо).")
        st.json(payload)
