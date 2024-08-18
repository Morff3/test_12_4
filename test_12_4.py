import unittest
import rt_with_exceptions
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            item_walk = rt_with_exceptions.Runner(10, 20)
            for i in range(10):
                item_walk.walk()
            self.assertEqual(item_walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно {item_walk}')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            item_run = rt_with_exceptions.Runner('Run2', -55)
            for i in range(10):
                item_run.run()
            self.assertEqual(item_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    def test_challenge(self):
        item_1 = rt_with_exceptions.Runner('Run3')
        item_2 = rt_with_exceptions.Runner('Run4')
        for i in range(10):
            item_1.walk()
            item_2.run()
        self.assertNotEqual(item_1.distance, item_2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
