from typing import List


violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]


def sum_3_songs_list(violator_songs_list: List[List], song_1: str, song_2: str, song_3: str):
    all_time_songs = 0
    for i in range(len(violator_songs_list)):
        if violator_songs_list[i][0] in [song_1, song_2, song_3]:
            all_time_songs += violator_songs_list[i][1]

    return f"Три песни звучат {round(all_time_songs, 2)} минут"

# print(sum_3_songs_list(violator_songs_list, 'Halo', 'Enjoy the Silence', 'Clean'))


violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def sum_3_songs_dict(violator_songs_dict: dict, song_1: str, song_2: str, song_3: str):
    vsd_name = list(violator_songs_dict.keys())
    vsd_values = list(violator_songs_dict.values())
    time_3_songs = 0
    other_times = 0

    for i in range(len(violator_songs_dict)):
        if vsd_name[i] in [song_1, song_2, song_3]:
            time_3_songs += vsd_values[i]
        else:
            other_times += vsd_values[i]

    return f"Общее время звучания трех песен: {round(time_3_songs, 2)}\nА другие три песни звучат {round(other_times, 2)} минут"

# print(sum_3_songs_dict(violator_songs_dict, 'Sweetest Perfection', 'Policy of Truth', 'Blue Dress'))