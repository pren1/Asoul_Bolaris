import live_data_summary
import tool_function as tf
import json
import pdb
import tqdm

# room_id, live_date, live_road, live_type = tf.get_arg()

def process_live_data(room_id, live_date, target_path="/home/admin/public/data/"):
    live_road = "%s_%s" % (live_date, room_id)
    live = live_data_summary.live_summary(my_room_id=room_id, my_live_date=live_date,
                                      my_live_road=live_road, target_path = target_path)
    live.get_everyday_live_stats()
    print("Everything gets done!")

if __name__ == '__main__':
    target_path = "/home/admin/public/data/"
    # target_path = '/Users/renpeng/Downloads/Bolaris/'
    process_live_data('22634198', '2021_9_10', target_path)

    live_json_readin = target_path + 'live_list.json'
    with open(live_json_readin) as json_file:
        live_list = json.load(json_file)

    for sig in tqdm(live_list):
        date = sig.split('&')[0]
        room_id = sig.split('&')[1]
        print(f"processing {date} at {room_id}...")
        process_live_data(room_id, date, target_path)