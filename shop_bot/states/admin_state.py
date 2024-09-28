from aiogram.fsm.state import State, StatesGroup


class FSMAdminPanel(StatesGroup):
    start_menu = State()
    choose_action = State()


class FSMSphereCRUD(StatesGroup):
    choose_sphere = State()
    crud_menu = State()
    create_sphere = State()
    delete_sphere = State()
    new_sphere_name = State()
    update_sphere_name = State()
    edit_profession = State()


class FSMProfessionCRUD(StatesGroup):
    choose_profession_or_action = State()
    crud_menu = State()
    delete_profession = State()
    new_profession_name = State()
    new_profession_url = State()
    update_profession_name = State()
    update_profession_url = State()

