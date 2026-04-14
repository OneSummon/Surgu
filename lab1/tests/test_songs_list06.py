import package


def test_sum_3_songs_list_always_returns_none():
    songs = [
        ['World in My Eyes', 4.86],
        ['Halo', 4.9],
        ['Enjoy the Silence', 4.20],
        ['Clean', 5.83],
    ]
    
    assert package.sum_3_songs_list(songs, 'Halo', 'Enjoy the Silence', 'Clean') is None

def test_sum_3_songs_list_empty_list():
    assert package.sum_3_songs_list([], 'Halo', 'Enjoy', 'Clean') is None


def test_sum_3_songs_dict_normal():
    songs_dict = {
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
    expected = "Общее время звучания трех песен: 13.49\nА другие три песни звучат 29.97 минут"
    assert package.sum_3_songs_dict(songs_dict, 'Sweetest Perfection', 'Policy of Truth', 'Blue Dress') == expected

def test_sum_3_songs_dict_missing_song():
    songs_dict = {'A': 1.0, 'B': 2.0, 'C': 3.0}
    assert package.sum_3_songs_dict(songs_dict, 'A', 'B', 'D') is None

def test_sum_3_songs_dict_empty_dict():
    assert package.sum_3_songs_dict({}, 'A', 'B', 'C') is None