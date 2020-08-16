import scala.io.StdIn.readLine

object Bela {
    def main(args: Array[String]) = {
        val DominantScores = Map(
            'A' -> 11,
            'K' -> 4,
            'Q' -> 3,
            'J' -> 20,
            'T' -> 10,
            '9' -> 14,
            '8' -> 0,
            '7' -> 0)

        val NotDominantScores = Map(
            'A' -> 11,
            'K' -> 4,
            'Q' -> 3,
            'J' -> 2,
            'T' -> 10,
            '9' -> 0,
            '8' -> 0,
            '7' -> 0)

        var score = 0
        val x = readLine().split(" ")
        val n = x(0).toInt
        val b = x(1)(0)

        for (i <- 0 until 4*n) {
            val line = readLine()
            val suit = line(1)
            val card = line(0)

            if (suit == b) {
                score += DominantScores(card)
            } else {
                score += NotDominantScores(card)
            }
        }
        println(score)
    }
}