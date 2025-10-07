
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
    "ГПО": "Группа продаж и обслуживания, целью которой является работа с действующими клиентами Ростелекома (продажа новых продуктов, допродажа дополнительных услуг по подключённым продуктам, решение проблем клиента).",
    "НПС": "Группа по работе с лояльностью клиентов. Цель — выявление причин оттока и удержание клиентов, например путём предоставления скидок на услуги Ростелекома или помощи в решении текущих проблем.",
    "НДС": "Направление по дистанционному сервису. Сотрудники работают в Управлении по дистанционному сервису и развитию клиентского портфеля.",
    "ГПХ": "Группа активных продаж, целью которой является продажа услуг Ростелекома. (Трудоустройство по ГПХ не является причиной выбора канала «ГПХ» — необходимо выбирать канал в соответствии с группой сотрудников, с которой предстоит работать.)",
    "ИТМ": "Группа исходящего телемаркетинга. В канале работает НОД — направление обработки дистанции, ответственное за обработку лидов от клиентов, обратившихся по дистанционным каналам: сайт RT.RU, звонок в контакт‑центр ПАО «Ростелеком», ЛК ЮЛ и пр.",
    "B2G": "Группа по работе с позициями ПГ.",
    "Средний сегмент": "Раздел для сотрудников канала ГПО, предназначенный для длительной работы с клиентами среднего сегмента: ведение и дополнение карточки клиента, осуществление продаж. Для предоставления этой роли также создаётся доступ в канале ГПО.",
    "ОКН": "Раздел для сотрудников канала ОКН, предназначенный для работы с объектами коммерческой недвижимости.",
    "3К": "Канал для работы с крупными корпоративными клиентами (3К) — подразделение продаж, ответственное за обработку лидов данного сегмента.",
    "ПДЗ и Ликвидированные": "Группа по работе с просроченной дебиторской задолженностью, реорганизацией и ликвидированными компаниями. Для предоставления этой роли также создаётся доступ в канале ГПО.",
    "Процесс ликвидации/реорганизации": "Группа по работе с компаниями, находящимися в процессе ликвидации или реорганизации. С такими клиентами необходимо перезаключить договор или присвоить статус «Ликвидирован». Для предоставления этой роли также создаётся доступ в канале ГПО.",
}

nonstandard_text = "Если вам необходимо нестандартное сочетание каналов или прав доступа, подробно опишите это в поле «Дополнительная информация»."

roles_general = ["Исполнитель","Групп-лидер","Руководитель канала","Руководитель каналов РД","Руководитель каналов КЦ"]
role_texts_general = {
    "Исполнитель": "Роль для менеджеров, которые непосредственно работают с назначенными лидами, клиентами и позициями ПГ. Исполнитель может работать только в одном канале.",
    "Групп-лидер": "Роль для руководителей групп, которые назначают лиды на менеджеров, работают с отчётностью по своим группам и при необходимости сами отрабатывают задания. Групп‑лидер может работать только в одном канале.",
    "Руководитель канала": "Роль для региональных руководителей каналов: назначение лидов на руководителей групп и менеджеров, работа с отчётностью, при необходимости самостоятельная отработка. Руководителю канала может быть доступно несколько каналов.",
    "Руководитель каналов РД": "Роль для руководителей на уровне РД, работающих с отчётностью. Самостоятельная отработка и назначение лидов не предусмотрены. В профиле руководителя РД может быть доступно несколько каналов и несколько РД.",
    "Руководитель каналов КЦ": "Роль для руководителей на уровне КЦ, работающих с отчётностью. Самостоятельная отработка и назначение лидов не предусмотрены. В профиле руководителя КЦ может быть доступно несколько каналов.",
}

roles_okn = ["Исполнитель","Менеджер сопровождения ОКН","Руководитель канала","Руководитель каналов РД","Руководитель каналов КЦ"]
role_texts_okn = {
    "Исполнитель": "Роль для менеджеров, которые работают с закреплёнными объектами ОКН.",
    "Менеджер сопровождения ОКН": "Роль для сотрудников, ведущих сопровождение финансово‑экономической деятельности ОКН. Пользователь, закреплённый как менеджер сопровождения, может редактировать поля карточки ОКН, менять статус объекта и переназначать исполнителя.",
    "Руководитель канала": "Роль для региональных руководителей каналов: назначение объектов ОКН на менеджеров, работа с отчётностью и при необходимости самостоятельная отработка.",
    "Руководитель каналов РД": "Роль для руководителей на уровне РД, работающих с отчётностью по ОКН. Назначение объектов и самостоятельная отработка не предусмотрены.",
    "Руководитель каналов КЦ": "Роль для руководителей на уровне КЦ, работающих с отчётностью по ОКН. Назначение объектов и самостоятельная отработка не предусмотрены.",
}

roles_with_extra_general = {"Руководитель канала","Руководитель каналов РД","Руководитель каналов КЦ"}
roles_with_extra_okn = {"Руководитель каналов КЦ"}

extra_channel_options = ["ГАП","ГПО","НПС","НДС","ГПХ","ИТМ","B2G","Средний сегмент","ПДЗ и Ликвидированные","Процесс ликвидации/реорганизации"]

RD_LIST = ["РД Центр","РД Северо‑Запад","РД Волга","РД Юг","РД Урал","РД Сибирь","РД Дальний Восток","РД Москва и Московская область"]
RF_BRANCHES = ["Белгородский филиал","Брянский филиал","Воронежский филиал","Калужский филиал","Магаданский филиал","Камчатский филиал","Амурский филиал","Сахалинский филиал","Хабаровский филиал","Филиал Сахателеком","Московский филиал"]

CHANNELS_DIRECT_RD = {"ИТМ","3К","ОКН","НДС","НПС"}

def render_main_layout(show_info_note: bool, show_extra_desc: bool):
    st.set_page_config(page_title=FORM_TITLE, page_icon="🧩", layout="centered")
    st.title("Предоставление доступа")

    # State
    if "extra_channels" not in st.session_state: st.session_state.extra_channels = []
    if "prev_role" not in st.session_state: st.session_state.prev_role = None
    if "prev_channel" not in st.session_state: st.session_state.prev_channel = None
    if "extra_rd" not in st.session_state: st.session_state.extra_rd = []
    if "level_select" not in st.session_state: st.session_state.level_select = None

    # Channel
    channel = st.selectbox(TRIGGER_CHANNEL, channels, index=None, placeholder="Выберите канал", key="main_channel")

    # Reset
    if channel != st.session_state.prev_channel:
        st.session_state.prev_channel = channel
        st.session_state.extra_channels = []
        st.session_state.extra_rd = []
        st.session_state.role_select = None
        st.session_state.level_select = None
        for k in ["gpo_mid","gpo_pdz","gpo_proc"]:
            st.session_state[k] = False

    # Description (plain, без голубого блока)
    if channel:
        if channel == "Нестандартная роль (подробно опишу в поле дополнительная информация)":
            st.markdown("*" + nonstandard_text + "*")
        else:
            desc = channel_descriptions.get(channel)
            if desc:
                st.markdown(desc)

    # ГПО чекбоксы
    if channel == "ГПО":
        st.write("Для сотрудников ГПО дополнительные каналы:")
        c1,c2,c3 = st.columns(3)
        with c1: st.checkbox("Средний сегмент", key="gpo_mid")
        with c2: st.checkbox("ПДЗ и Ликвидированные", key="gpo_pdz")
        with c3: st.checkbox("Процесс ликвидации/реорганизации", key="gpo_proc")

    # Role set
    selected_role = None
    roles_list = []; role_texts_map = {}; roles_with_extra = set()
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

                # Extra channel rows
                if selected_role in roles_with_extra:
                    if st.button("Добавить дополнительный канал"):
                        st.session_state.extra_channels.append(None)

                    to_remove = []
                    for i,_ in enumerate(st.session_state.extra_channels):
                        sel_col, btn_col = st.columns([6,1], vertical_alignment="bottom")
                        with sel_col:
                            st.session_state.extra_channels[i] = st.selectbox(
                                "",
                                extra_channel_options,
                                index=None,
                                placeholder="Дополнительный канал",
                                key=f"extra_channel_{i}",
                                label_visibility="collapsed"
                            )
                        with btn_col:
                            if st.button("Удалить", key=f"del_extra_channel_{i}"):
                                to_remove.append(i)

                        # v2: show description under each extra channel
                        if show_extra_desc and st.session_state.extra_channels[i]:
                            ch = st.session_state.extra_channels[i]
                            d = channel_descriptions.get(ch)
                            if d:
                                st.caption(d)
                    for idx in reversed(to_remove):
                        del st.session_state.extra_channels[idx]

                    # Info note (plain text, no blue)
                    if show_info_note and channel in {"ИТМ","НДС","НПС"} and st.session_state.extra_channels:
                        st.markdown("ℹ️ Учётные записи для каналов **ИТМ**, **НДС** и **НПС** создаются на уровне региональных дирекций. Если необходимо работать с лидами региональных филиалов, создайте отдельную учётную запись.")

    # Regions
    hide_regions = (selected_role == "Руководитель каналов КЦ")
    selected_rd = None; selected_level = None; selected_rf_branch = None

    if not hide_regions and channel:
        if channel in CHANNELS_DIRECT_RD:
            selected_rd = st.selectbox("Укажите РД, в котором необходимо создать учётную запись:", RD_LIST, index=None, placeholder="Выберите РД", key="rd_direct")
            if st.button("Добавить ещё одну региональную дирекцию"):
                st.session_state.extra_rd.append(None)
            to_remove_rd = []
            for i,_ in enumerate(st.session_state.extra_rd):
                sel_col, btn_col = st.columns([6,1], vertical_alignment="bottom")
                with sel_col:
                    st.session_state.extra_rd[i] = st.selectbox("", RD_LIST, index=None, placeholder="Дополнительный РД", key=f"extra_rd_{i}", label_visibility="collapsed")
                with btn_col:
                    if st.button("Удалить", key=f"del_extra_rd_{i}"):
                        to_remove_rd.append(i)
            for idx in reversed(to_remove_rd):
                del st.session_state.extra_rd[idx]
        else:
            selected_level = st.selectbox("Учётную запись необходимо создать на уровне:", ["РФ (Региональный филиал)","РД (Региональная дирекция)"], index=None, placeholder="Выберите уровень", key="level_select")
            if selected_level == "РФ (Региональный филиал)":
                selected_rf_branch = st.selectbox("Выберите филиал РФ:", RF_BRANCHES, index=None, placeholder="Выберите филиал", key="rf_branch")
            elif selected_level == "РД (Региональная дирекция)":
                selected_rd = st.selectbox("Выберите РД:", RD_LIST, index=None, placeholder="Выберите РД", key="rd_level")
                if st.button("Добавить ещё одну региональную дирекцию"):
                    st.session_state.extra_rd.append(None)
                to_remove_rd = []
                for i,_ in enumerate(st.session_state.extra_rd):
                    sel_col, btn_col = st.columns([6,1], vertical_alignment="bottom")
                    with sel_col:
                        st.session_state.extra_rd[i] = st.selectbox("", RD_LIST, index=None, placeholder="Дополнительный РД", key=f"extra_rd_{i}", label_visibility="collapsed")
                    with btn_col:
                        if st.button("Удалить", key=f"del_extra_rd_{i}"):
                            to_remove_rd.append(i)
                for idx in reversed(to_remove_rd):
                    del st.session_state.extra_rd[idx]

    # Bottom
    st.divider()
    add_info_required = (channel == "Нестандартная роль (подробно опишу в поле дополнительная информация)")
    add_info_label = "Дополнительная информация:" + (" *" if add_info_required else "")
    add_info = st.text_area(add_info_label, height=140, key="extra_info")
    contact_method = st.selectbox("Удобный способ взаимодействия:", ["Мобильный телефон","Почта"], index=None, placeholder="Выберите способ", key="contact_method")

    st.divider()
    if st.button("Отправить заявку"):
        errors = []
        if not channel:
            errors.append("Выберите канал.")
        need_role = channel and channel != "Нестандартная роль (подробно опишу в поле дополнительная информация)"
        if need_role and not selected_role:
            errors.append("Выберите роль.")
        if not hide_regions and channel:
            if channel in CHANNELS_DIRECT_RD:
                if selected_rd is None:
                    errors.append("Выберите региональную дирекцию (РД).")
            else:
                if not selected_level:
                    errors.append("Выберите уровень (РФ/РД).")
                else:
                    if selected_level.startswith("РФ") and not selected_rf_branch:
                        errors.append("Выберите филиал РФ.")
                    if selected_level.startswith("РД") and selected_rd is None:
                        errors.append("Выберите региональную дирекцию (РД).")
        if add_info_required and not (add_info or "").strip():
            errors.append("Заполните поле «Дополнительная информация».")
        if not contact_method:
            errors.append("Выберите удобный способ взаимодействия.")

        if errors:
            st.error("\n".join("• " + e for e in errors))
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
                "Региональный уровень": None if (selected_role == "Руководитель каналов КЦ") else {
                    "Тип выбора": ("Прямой выбор РД" if channel in CHANNELS_DIRECT_RD else selected_level),
                    "РД (основной)": selected_rd,
                    "Филиал РФ": selected_rf_branch,
                    "Доп. РД": [r for r in st.session_state.extra_rd if r],
                },
                "Доп. информация": (add_info or "").strip(),
                "Контакт": contact_method,
            }
            st.success("Заявка отправлена (демо).")
            st.json(payload)


if __name__ == '__main__':
    render_main_layout(show_info_note=True, show_extra_desc=True)
