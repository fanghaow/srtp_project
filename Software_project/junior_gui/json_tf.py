import json
import numpy as np
import matplotlib.pyplot as plt
class Json_Tf():
    def __init__(self):
        self.filename = 'Grape_data.json'
        self.clear_file
        pass

    def clear_file(self):
        pass

    def json_1D(self, fruit_data_up):
        wave_length_up = [i for i in range(256)]
        py_list_up = []
        for i in range(256):
            py_dict_up = {}
            py_dict_up[wave_length_up[i]] = fruit_data_up[i]
            py_list_up.append(py_dict_up)
        json_data = open(self.filename, 'w')
        json.dump(py_list_up, json_data, ensure_ascii=False, indent=4)
        json_data.close()
        print('Save data into json file successfully!!!')

    def json_2D(self, strength):
        # Write a (time * 256) matrix into json file
        # Check how many times json has
        json_data = open(self.filename, 'r', encoding='utf-8')
        py_list_down = json.load(json_data)
        json_data.close()
        time_old = len(py_list_down)
        data_mat = np.zeros((time_old, 256))
        order = 0
        for key, value in py_list_down.items():
            data_mat[order, :] = value
            order += 1
        # Save new data
        new_vector = np.array(strength)
        data_mat = np.vstack((data_mat, new_vector))
        data_mat = list(data_mat)
        data_mat = [list(i) for i in data_mat]
        data_dict = {}
        for t in range(time_old + 1):
            data_dict['Number ' + str(t + 1) + ' times'] = data_mat[t]
        json_data = open(self.filename, 'w')
        json.dump(data_dict, json_data, ensure_ascii=False, indent=4)
        json_data.close()
        print('save successfully')

def main():
    jt = Json_Tf()
    strength = [i for i in range(256)]
    jt.json_2D(strength)

if __name__ == '__main__':
    main()