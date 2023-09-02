import text
import viev
import model


def search_block(msg: str):
    request = viev.input_request(msg)
    result = model.search(request)
    viev.show_book(result, text.not_search(request))
    if result:
        return True
    

def start():
    while True:
        choice = viev.menu()
        match choice:
            case 1:
                model.open_file()
                viev.print_message(text.file_load_successful)
            case 2:
                model.save_file()
                viev.print_message(text.file_save_successful)
            case 3:
                book = model.phone_book
                viev.show_book(book, text.empty_phone_book)
            case 4:
                contact = viev.input_contact(text.new_contact)
                model.add_contact(contact)
                viev.print_message(text.contact_save_successful(contact[0], text.contact_operation[0]))
            case 5:
                search_block(text.for_search)
            case 6:
                if search_block(text.for_edit):
                    edit_id = int(viev.input_request(text.input_edit_id))
                    new_contact = viev.input_contact(text.input_edit_contact)
                    name = model.edit(edit_id, new_contact)
                    viev.print_message(text.contact_save_successful(name, text.contact_operation[1]))
            case 7:
                if search_block(text.for_delete):
                    del_id = int(viev.input_request(text.input_del_id))
                    name = model.del_contact(del_id)[0]
                    viev.print_message(text.contact_save_successful(name, text.contact_operation[2]))
            case 8:
                if model.phone_book != model.original_book:
                    if viev.input_request(text.confirm_changes).lower() == 'y' or 'у':
                        model.save_file()
                        viev.print_message(text.file_save_successful)
                viev.print_message(text.end_program)
                break