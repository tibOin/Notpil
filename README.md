# Notpil

I was on a well-know site (no spoil so no quote) trying to solve a challenge
consisting of solving a captcha in less than 3 seconds.
Documentation related to this challenge oriented me on using python to do this.

I didn't know python until there and was a little bit intimidated by this language
with a syntax I didn't learned and the huge amount of libraries available.

But I took my courage by 2 hands *(as french people says : "Prendre son courage à deux mains")* and decided to try using python.

Little Google search on manipulating images with python brought me to PIL and OpenCV.
I already used a bit OpenCV with C++ so I decided to try this. Nice! But too heavy.
Then a looked at PIL. Good surprise! it's powerful and easy to use. Perfect.

After some searches on Google and PIL Documentation, and the great idea of removing noise that was black pixels while the text was gray. Pass it to tesseract and Boom! challenge solved.

The day before, I never thought I'd be able to do that.

Strong of this experience, I thought I was going to try a more complicated one.

Found the one [here](images/securimage.png).

I the wrote the script [Notpil.py](notpil.py).
Not really clean, but it's a prototype and I'm an amateur.

TODO :
+ ~~Remove all that is not in same color as text.~~
+ ~~Binarize the image to get it black and white.~~
+ ~~Remove noise *(Black dots on the image)*~~
+ ~~Fill the wholes leaved by color cleaning~~

Now I'm stuck :
+ How to rebuild characters ?
+ And how to remove the deformation of the text ?
