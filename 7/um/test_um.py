from um import count


def test_symbol_after_um():
    assert count("Um?") == 1
    assert count("Hello, um!") == 1
    assert count("Um, what's up.")


def test_start_works():
    assert count("um") == 1
    assert count("Um, are you sure you're alright?") == 1


def test_space_is_before():
    assert count("Yummy") == 0
    assert count("Would you like a cucumber?") == 0
    assert count("Im assuming you would like to exit this argument, and eat sume cucumbers instead.") == 0 # On purpose type errors.


def test_case_insensitive():
    assert count("UM! WHERE DO YOU THINK YOU ARE GOING?!?!") == 1
    assert count("Hello uM... what umm.. are you doing Uumm... this um, weekend?") == 2


def test_CS50():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_nomal():
    assert count("Hello um, ive been meaning of ask you... ") == 1
    assert count("um") == 1
    assert count("Um, i think you're friend is looking at me?")
