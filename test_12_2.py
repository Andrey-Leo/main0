import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrei = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_tournament_1(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    def test_tournament_2(self):
        tournament = Tournament(90, self.andrei, self.nick)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    def test_tournament_3(self):
        tournament = Tournament(90, self.usain, self.andrei, self.nick)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
