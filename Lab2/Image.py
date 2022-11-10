from GrayScale import _GrayScaleTransform
from ImageComparison import _ImageComparison
from BaseImage import _BaseImage
from ColorModel import _ColorModel

class _Image(_GrayScaleTransform, _ImageComparison):
    """
    klasa stanowiaca glowny interfejs biblioteki
    w pozniejszym czasie bedzie dziedziczyla po kolejnych klasach
    realizujacych kolejne metody przetwarzania obrazow
    """
    def __init__(self) -> None:
        super().__init__()