from models.state import StateModel
import re
from config.populate_table import empty_table,fill_table

class StateResource():
    @classmethod
    def move(cls,data):

        option = int(re.sub('\n','',data).strip())
        if option in (1,2,3):
            try:
                current_state = StateModel.get_current_state()
                new_state = cls.find_next(current_state,option)
            except:
                return 'Server Error'
        else:
            return 'Incorrect Input'

        return new_state.name
    
    @classmethod
    def find_next(cls,current_state,option):
        destination = 'dest_'+str(option)
        new_state_id = getattr(current_state, destination)
        new_state = StateModel.get_state_by_id(new_state_id)
        current_state.is_active=False
        new_state.is_active=True
        current_state.update()
        new_state.update()
        return new_state