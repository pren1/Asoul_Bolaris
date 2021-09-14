import live_data_summary
import tool_function as tf
import json
import pdb
from tqdm import tqdm

# room_id, live_date, live_road, live_type = tf.get_arg()

def process_live_data(room_id, live_date, target_path="/home/admin/public/data/"):
    live_road = "%s_%s" % (live_date, room_id)
    live = live_data_summary.live_summary(my_room_id=room_id, my_live_date=live_date,
                                      my_live_road=live_road, target_path = target_path)
    return live.get_everyday_live_stats()

if __name__ == '__main__':
    target_path = "/home/admin/public/data/"
    # target_path = '/Users/renpeng/Downloads/Bolaris/'
    # process_live_data('22637261', '2021_8_26', target_path)
    # process_live_data('22637261', '2021_8_5', target_path)
    # process_live_data('22637261', '2021_8_12', target_path)
    # process_live_data('22637261', '2021_8_19', target_path)
    # process_live_data('22625027', '2021_6_30', target_path)
    # pdb.set_trace()

    live_json_readin = target_path + 'live_list.json'
    with open(live_json_readin) as json_file:
        live_list = json.load(json_file)

    real_live_list = []
    for sig in tqdm(live_list):
        date = sig.split('&')[0]
        room_id = sig.split('&')[1]
        print(f"processing {date} at {room_id}...")
        if process_live_data(room_id, date, target_path):
            real_live_list.append(sig)

    print(f"real live list: {real_live_list}")
    with open(f"{target_path}/real_live_list.json", "w", encoding='utf8') as outfile:
        json.dump(real_live_list, outfile, ensure_ascii=False)