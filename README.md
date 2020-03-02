Appropriate Kanji Generator
----
*For the lack of a better title*

Given input and a grade level, filters out non-grade appropriate kanji from a document.  Allows you to replace w/ Hiragana or Furigana

An example is available [here](http://jbm-kanji-generator.herokuapp.com/).

Input Format
----
Currently, the parsing format is primitive.  The parser looks for a bracket after a Kanji, and then a reading therein.

Example:
我(わが)輩(はい)

In some cases, the *kanji* may be taught at a certain grade level, but the *reading* used is not necessarily taught until later on.  You can use a pipe to override the normal grade level assigned to the Kanji.

Example:
土(み|9）産（やげ|9)

If you are using English-language brackets in the text, this won't parse correctly.
 
Changing Kanji Display Logic
----

The Kanji display method is set in the `kanji_grade_alignment_tool.py` file.  Currently, we use the `reading_level` (the grade at which the Kanji is taught or the overridden value in the brackets) and the `grade` (student grade) to determine what should be displayed.  

For more complex behavior around furigana, you can create a function similar to `basic_text` and `furigana_html` and pass it into `set_appropriate_kanji`.

Things that need work
----
1. How to handle multiple readings of a word (日本 as ニホン or にっぽん)
2. Situations where multiple kanji together have a reading, but an individual kanji doesn't.  (韓国 being given the non-standard reading コリア) 
3. Easier way to import documents and work on them (and make them available for other people to reuse)
4. Unbalanced brackets ;-)