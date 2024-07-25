Welcome! To use my project titled Vibelyze, you will have to run the command python app.py. After this, there will be a link that forwards you to the website. Once you are at the website or main user interface, you will see two text blocks. One asks for a movie input so you can put the name of the movie that is going to be reviewed. Then, another one asks the user for a text of any length that reviews this movie. For example, you can type the movie "Interstellar" and then submit a prompt "I Loved this movie." Then, the computer will analyze the sentence provided and tell the user whether based on the language used in that review, it recommends this movie or not.
Additionally, you can run this program multiple times. After getting an analysis done by the computer on a movie, you can input the name of any other movie and input a different text and the computer will again tell the user if it is a good or bad movie to watch. A little tip when using the program: let's say you inputted a bad review, and the computer said it doesn't recommend it, if you are trying to test it out and let's say you are preemptively going to input another bad review, to see if it works correctly you should input a rating like 10/10 first to change the computers analysis so you can see it correctly change when you input the new negative review.
Keep in mind that this project was done without the use of importing sophisticated libraries or the use of PyTorch. Instead, I created my own database of words and gave them all either a positive, neutral, or negative assigned value. And so complexities like "I did not love this movie" may return incorrect sentiment analysis from the computer as it will presume that since the word love is there it is positive, however, we can see it is not. However, the model that I ran is still built on over 1000+ words and does handle some other complexities. For example, if the user inputs a bad review of a movie that is generally very loved by the public and highly acclaimed, for example, The Shawshank Redemption, the program will not just say it doesn't recommend this movie, instead it will say "This is a negative review. However, generally, many other people recommend this movie."
Overall, the program is pretty simple to use. So, I invite you to test the program out. Input your favorite movies and test how well the database can handle certain complexities.
Youtube URL: https://youtu.be/_gb3fPuvewk