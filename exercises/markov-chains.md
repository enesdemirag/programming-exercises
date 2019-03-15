### Theoretical - Markov Chains

A Markov Chain is a sequence of states. The idea of a sequence means, there should always be a transition where the state goes from one state to another.

For example, You could think of the behaviors of a baby as a Markov Chain Model, you might include **playing, eating, sleeping, and crying** as states, which together creates a **state space**, a list of all possible states. A typical sequence can be like (play --> eat --> sleep --> cry). A Markov Chain tells you the probability of transition from one state to any other state.

<p align="center">
  <img src="https://web.itu.edu.tr/demirag16/img/markov-chain.gif">
</p>

Marcov Chains used in a variety of fields to analyze a sequence of states and also generate or predict outcomes based on that sequence such as financial data, scientific data, weather patterns, or predicting an earthquake based on sensor readings. You can look [this great visual explanation](http://setosa.io/ev/markov-chains/) of Marcov Chains.  

We can generate a sequence of states based on existing states and probability of outcomes after that.
And also we can think of text as a sequence of states. Every character represents a state. Or we could also think text as a sequence of states on word level.

As a result, we can adjust probabilities of states (words or characters) based of an existing source text.
Besides each state can be a single word or character, also there is a concept known as **_n-gram._** n-gram is a contiguous sequence of n states from a given sequence. n-gram models widely used in Communication Theory and Natural Language Processing. You can check Google's [n-gram Viewer](https://books.google.com/ngrams) and see the frequency of every word or sequence of words. Also [here is a awesome visualization](http://www.chrisharrison.net/index.php/Visualizations/WebTrigrams) of Tri-Grams.

[Here](https://youtu.be/eGFJ8vugIWA) is a video on generating text using character level n-grams in JavaScript.


### Practical - Markov Chains

todo
