import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test per GIOIA
        statement_1 = "I am glad this happened"
        label_1 = emotion_detector(statement_1)['dominant_emotion']
        self.assertEqual(label_1, 'joy')

        # Test per RABBIA
        statement_2 = "I am really mad about this"
        label_2 = emotion_detector(statement_2)['dominant_emotion']
        self.assertEqual(label_2, 'anger')

        # Test per DISGUSTO
        statement_3 = "I am feel disgusted just hearing about this"
        label_3 = emotion_detector(statement_3)['dominant_emotion']
        self.assertEqual(label_3, 'disgust')

        # Test per TRISTEZZA
        statement_4 = "I am so sad about this"
        label_4 = emotion_detector(statement_4)['dominant_emotion']
        self.assertEqual(label_4, 'sadness')

        # Test per PAURA
        statement_5 = "I am really afraid that this will happen"
        label_5 = emotion_detector(statement_5)['dominant_emotion']
        self.assertEqual(label_5, 'fear')

if __name__ == '__main__':
    unittest.main()