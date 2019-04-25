# Natural Language Processing Stuff
import lyricScrub
from nltk.tokenize import WhitespaceTokenizer
from nltk.corpus import cmudict

wordList = {
    "knowin'": ["N", "OW1", "IH0", "N"],
    "mo'": ["M", "OW1"],
    "fo'": ["F", "OW1"],
    "mo's": ["M", "OW1", "Z"],
    "fo's": ["F", "OW1", "Z"],
    "phat": ["F", "AE1", "T"],
    "don’t": ["D", "OW1", "N", "T"],
    "wanna": ["W", "AH2", "N", "AH1"],
    "understand?": ['AE1', 'N']
}
keyList = []
vowels = [
    "AA0", "AE0", "AH0", "AO0", "AW0", "AY0", "EH0", "EY0", "IH0", "IY0",
    "OW0", "OY0", "UH0", "UW0", "AA1", "AE1", "AH1", "AO1", "AW1", "AY1",
    "EH1", "EY1", "IH1", "IY1", "OW1", "OY1", "UH0", "UW1", "AA2", "AE2",
    "AH2", "AO2", "AW2", "AY2", "EH2", "EY2", "IH2", "IY2", "OW2", "OY2",
    "UH2", "UW2", "ER1"
]

skipWords = [
    'the', "and", 'their', 'yeah', "that's", "then", "there", "as", "it", "is",
    "when", "they", "if", "in"
]
vowelDict = {}


# Create a dictionary with vowel sounds as keys and the words with that sound
# as the values. Then, highlight words according to their vowel sound.
def highlighter(lyrics):
    for i in range(0, len(vowels)):
        vowelDict[vowels[i]] = []
    for i in range(0, len(vowels)):
        for k in range(0, len(keyList)):
            if vowels[i] in wordList[keyList[k]]:
                if keyList[k] not in vowelDict.values():
                    vowelDict[vowels[i]].append(keyList[k])
    end = '</span>'
    global Lyrics
    for i in range(0, len(lyrics)):
        if lyrics[i] == 'nike':
            lyrics[
                i] = '<span style="background-color: #cc99ff;">nik</span><span style="background-color: #ffcc99;">e' + end
        if lyrics[i] in vowelDict['IY1'] or lyrics[i] in vowelDict[
                'IY2'] or lyrics[i] in vowelDict['IY0']:
            lyrics[i] = '<span style="background-color: #ffcc99;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['OW0'] or lyrics[i] in vowelDict[
                'OW1'] or lyrics[i] in vowelDict['OW1']:
            lyrics[i] = '<span style="background-color: #cfb480;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['AO1']:
            lyrics[i] = '<span style="background-color: #ccffcc;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['AH1'] or lyrics[i] in vowelDict[
                'AH2'] or lyrics[i] == 'wanna':
            lyrics[i] = '<span style="background-color: #fc5d5d;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['EY1'] or lyrics[i] in vowelDict['EY2']:
            lyrics[i] = '<span style="background-color: #ffff99;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['AY1'] or lyrics[i] in vowelDict['AY2']:
            lyrics[i] = '<span style="background-color: #cc99ff;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['AE1'] or lyrics[i] in vowelDict['AE2']:
            lyrics[i] = '<span style="background-color: #99ccff;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['ER1']:
            lyrics[i] = '<span style="background-color: #ed95d3;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['EH1'] or lyrics[i] in vowelDict['EH2']:
            lyrics[i] = lyrics[
                i] = '<span style="background-color: #89e8e6;">' + lyrics[
                    i] + end
        if lyrics[i] in vowelDict['OY1'] or lyrics[i] in vowelDict['OY2']:
            lyrics[i] = '<span style="background-color: #95ff80;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['AW0'] or lyrics[i] in vowelDict[
                'AW1'] or lyrics[i] in vowelDict['AW2']:
            lyrics[i] = '<span style="background-color: #f7abd1;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['UW0'] or lyrics[i] in vowelDict[
                'UW1'] or lyrics[i] in vowelDict['UW2']:
            lyrics[i] = '<span style="background-color: #ccf069;">' + lyrics[
                i] + end
        if lyrics[i] in vowelDict['IH0'] or lyrics[i] in vowelDict[
                'IH1'] or lyrics[i] in vowelDict['IH2']:
            lyrics[i] = '<span style="background-color: #ff70a0;">' + lyrics[
                i] + end
    Lyrics = ' '.join(lyrics)


# SPLITS SONG INTO VERSES
def get_Lyric_Sounds():
    superSong = ''.join(lyricScrub.LYRICS)

    # Allows lines to be reprinted as new lines when necessary
    mytext = " <br/> ".join(superSong.split("\n"))

    mytext2 = " ".join(mytext.split("-"))  # Splits hyphenated words

    # Seperates each word in the lyrics and adds them to a list.
    songLyrics = WhitespaceTokenizer().tokenize(mytext2)
    for i in range(0, len(songLyrics)):
        # Makes the search in the next for-loop faster and more accurate
        songLyrics[i] = songLyrics[i].lower()

        # Words with commas aren't included in dictionary
        songLyrics[i] = songLyrics[i].replace(",", "") 


    # Fetches the pronunication of each word and stores it in a dictionary
    for (word, pron) in cmudict.entries():
        if word in songLyrics:
            if word not in skipWords: # WordList does not include specified words.
                wordList[word] = pron

    # Creates a list of 
    for key in wordList:
        if len(wordList[key]) > 1:
            keyList.append(key)
    highlighter(songLyrics)
