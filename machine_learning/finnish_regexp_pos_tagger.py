import nltk, sys
import re

class FinnishRegexpPosTagger:

    PATTERNS = [
        # PUNCTUATION
        (r'[,\.\?\!\(\)\[\]\{\}\-]', 'PUNCT'),
        
        # SYMBOLS
        (r'[%@#\$\&\*\\]', 'SYM'),
        (r'\:\)|\:\(', 'SYM'), # smileys

        # NUMERALS
        (r'\d', 'NUM'), # digits
        (r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', 'NUM'), # roman numbers
        (r'[Nn]olla|[Yy]ksi|[Kk]aksi|[Kk]olme|[Nn]eljä|[Vv]iisi|[Kk]uusi|[Ss]eitsemän|[Kk]ahdeksan|[Yy]hdeksän|[Kk]ymmenen', 'NUM'), # basic
        (r'[Ss]ata|[Tt]uhat|[Mm]iljoona|[Mm]iljardi|[Bb]iljoona|toista|sataa', 'NUM'),
        
        # COORDINATING CONJUCTIONS
        (r'\b[Jj]a\b|\b[TtVv]ai\b|\b[Mm]utta\b|\b[Ee]li\b|\b[Kk]uin\b|\b[Nn]iin\b', 'CCONJ'),
        (r'\b[Ss]ekä\b|\b[Ee]ttä\b|\b[Jj]oko\b|\b[Tt]ahi\b|\b[Tt]aikka\b|\b[Ss]illä\b', 'CCONJ'),

        # SUBORDINATING CONJUCTIONS
        (r'\b[Kk]oska\b|\b[Vv]aikka\b|\b[Pp]arempi\b|\b[Kk]uin\b|\b[Jj]os\b|\b[Jj]otta\b|\b[Ee]t\b|\b[Kk]uha\b|\b[Kk]unhan\b', 'SCONJ'),
        (r'\b[Jj]olle(i|n|t|mme)?(vat|vät)?t?e?\b', 'SCONJ'), 

        # PERSONAL PRONOUNS
        (r'\b[MmSs]inä\b|\b[Hh]än\b|\b[MmTtHh]e\b', 'PRON'), # nominative
        (r'\b[MmSs]inua\b|\b[Hh]äntä\b|\b[MmTtHh]eitä\b', 'PRON'), # partitive
        (r'\b[MmSs]inun\b|\b[Hh]änen\b|\b[MmTtHh]eidän\b', 'PRON'), # genetive
        (r'\b[MmSs]inuun\b|\b[Hh]äneen\b|\b[MmTtHh]eihin\b', 'PRON'), # Keneen?
        (r'\b[MmSs]inussa\b|\b[Hh]änessä\b|\b[MmTtHh]eissä\b', 'PRON'), # Kenessä?
        (r'\b[MmSs]inusta\b|\b[Hh]änestä\b|\b[MmTtHh]eistä\b', 'PRON'), # Kenestä?
        (r'\b[MmSs]inull[ae]\b|[Hh]änell[äe\b]|\b[MmTtHh]eill[äe]\b', 'PRON'), # Kenellä? Kenelle?
        (r'\b[MmSs]inulta\b|\b[Hh]äneltä\b|\b[MmTtHh]eiltä\b', 'PRON'), # Keneltä?
        
        # INTERROGATIVE PRONOUNS
        (r'\b[Kk]uka\b|\b[Kk]etkä\b|\b[Kk]eitä\b|\b[Kk]uinka\b', 'PRON'),
        (r'\b[Mm]it?kä\b|\b[Mm]isstä\b|\b[Mm]istä\b|\b[Mm]ihin\b', 'PRON'),
        (r'\b[Mm]inne\b|\b[Mm]illt?ä\b|\b[Mm]ille\b|\b[Mm]iksi\b', 'PRON'),
        (r'\b[Mm]illainen\b|\b[Mm]illaiset\b|\b[Mm]illais[ie]sta\b|\b[Mm]illaista\b', 'PRON'),
        (r'\b[Mm]illaisia\b|\b[Mm]illoin\b|\b[Mm]iten\b', 'PRON'),     
        
        # DEMONSTRATIVE PRONOUNS
        (r'\b[Tt]ä[mthsl]s?l?t?ä?e?n?\b', 'PRON'), # tämä, all cases
        (r'\b[Tt]uo[tnhsl][aostl]?[nae]?\b', 'PRON'), #tuo, all cases
        (r'\b[Ss]en?|[Ss][ei][tnil][änhtl]e?ä?n?\b', 'PRON'), #se, all cases
        (r'\b[Nn]ä[im](ssä)?(stä)?(ll)?(ltä)?(hin)?(den)?t?ä?e?\b', 'PRON'), # nämä, all cases
        (r'\b[Nn]uo|[Nn](oi)(den)?(hin)?(ss)?(st)?(ll)?(lt)?t?[ae]?\b', 'PRON'), # nuo, all cases
        (r'\b[Nn]e|[Nn]i{2}(den)?(hin)?(ss)?(st)?(ll)?(lt)?t?ä?e?\b', 'PRON'), # ne, all cases

        # RELATIVE PRONOUNS
        (r'\b[Jj]ok?t?(nk)?(ho)?(ss)?(st)?(ll)?(lt)?a?e?n?\b', 'PRON'), # joka, all cases
        (r'\b[Jj]otka|[Jj]oi[kt]?(den)?(hin)?(ss)?(st)?(ll)?(lt)?a?e?\b', 'PRON'), # jotka, all cases
        (r'\b[Mm]i[ktnhsl](ä|kä|in|sä|tä|le|lä)', 'PRON'), # mikä, all cases

        # REFLEXIVE PRONOUNS
        (r'\b[Ii]tsee?ä?(ni)?(ss)?(st)?(ll)?(lt)?e?ä?(ni)?(mme)?\b', 'PRON'),

        # MUU, SAMA
        (r'\b[Mm]u{1,2}[aint]?(ll)?(den)?(lt)?(ks)?(tt)?(ss)?(st)?(hu)?(hi)?(oin)?[tn]?[iea]?\b', 'PRON'),
        (r'\b[Ss]am[ao]i?t?(ss)?(jen)?(st)?(ihi)?(iss)?(ist)?(ll)?(lt)?(ksi)?(tt)?j?n?e?a?n?\b', 'PRON'),
        
        # VERBS
        (r'\b[Ee]n\b|[Ee]t\b|[Ee]i\b|[Ee]mme\b|[Eette]\b|[Ee]ivät\b', 'VERB'),
        (r'\w*[aäiyueoö]{1}(mme|tte|vat|vät)\b', 'VERB'), # verbityypy1 plural forms
        (r'\w*(tse){1}(n|t|e|mme|tte|vät)\b', 'VERB'), # verbityypy 5
        (r'\w*(li)\b', 'VERB'),
        (r'\w*ahtaa\b', 'VERB'),

        # AUXILIARY VERBS
        (r'\b[Oo]lla\b|\b[Oo]n\b|\b[Oo]vat\b|\b[Oo]l(en|et|emme|ette)\b', 'AUX'), # olla, active, present
        (r'\b[Oo]li(n|t|mme|tte|vat)\b|\b[Oo]li\b', 'AUX'), # olla, active, imperfect
        (r'\b[Oo]llut\b|\b[Oo]lleet\b', 'AUX'), # olla, perfect
        (r'\b[Oo]lisi(n|t|mme|tte|vat)?\b', 'AUX'), # olla, active, conditional
        (r'\b[Tt]äy[td]y?(yy|nyt|i|kö|ne|ä|minen|mistä)?(si|ön)?', 'AUX'), # täytyä
        (r'\b[Pp]i[td][eäi]n?ä?(yt|neet|mme|eet|tt|tään|vät|isi)?(mme|tte|vät|y|kö|e|ä|mä)?(neen|vä|tön|stä|än|llä|ttä|män|n|minen|mistä)?', 'AUX'), # pitää
        (r'\b[Tt]arvit?a?(se|nn)?[nte]?(ma|si|kaa)?(mme|tte|vat|tu|ut|an|et|iin|aisi|ko|si)?(mme|tte|vat|in|akoon|ako|ks)?(ee)?(ssa|sta|lla)?[ntu]?', 'AUX'),
        
        # ADVERBS
        (r'\w*sti\b', 'ADV'),
        (r'\w*mmin\b', 'ADV'),
        (r'\w*immin\b', 'ADV'),
        (r'\w*iten\b', 'ADV'),
        (r'\b[Yy]hä\b|\b[Kk]uin\b', 'ADV'),

        # ADJECTIVES
        (r'\b\w*inen\b', 'ADJ'), # -inen adjectives
        (r'\b\w*nut\b', 'ADJ'), # -nut adjectives
        (r'\b\w*nyt\b', 'ADJ'), # -nyt adjectives
        (r'\b\w*mpi\b', 'ADJ'), # comparative
        (r'\w*toon\b', 'ADJ'), # alkoholitoon a podobný srandy
        (r'\w*mainen\b', 'ADJ'),
        (r'\w*hko\b', 'ADJ'),



        # ADPOSITIONS
        (r'\b[Ee]nnen\|\b[Aa]lla\b|\b[Pp]ällä\b|\b[Kk]anssa\b|\b[Ii]lman\b', 'ADP'),
        (r'\b[Vv]ailla\b|[Pp]itkin|[Aa]las|[Yy]lös', 'ADP'),

        # NOUNS
        (r'.*', 'NOUN')

        ]


    def __init__(self, filepath):
        """ Initialize the object: 
        1) store the path of the file containing POS-tagged Finnish
        text in the private variable __filepath
        2) create a regexp tagger for the patterns that you have defined
        and store the tagger in a private variable __regexp_tagger

        Don't change anything here.
        """
        self.__filepath = filepath
        self.__regexp_tagger = nltk.RegexpTagger(FinnishRegexpPosTagger.PATTERNS)


    def read_tagged_sents(self):
        """ This method reads the file at self.__filepath and extracts
        all the tagged sentences from the file (for evaluation purposes).
        The return value of this method consists of a list of
        lists. On the highest level, we have a list of
        sentences. Then, every sentence consists of a list of
        tuples. Every tuple is a pair of a word and its POS
        tag.

        Example snippet of the data structure that is returned:
        [[('Kävelyreitti', 'NOUN'), ('III', 'ADJ')], [('Jäällä',
        'NOUN'), ('kävely', 'NOUN'), ('avaa', 'VERB'), ('aina',
        'ADV'), ('hauskoja', 'ADJ'), ('ja', 'CONJ'), ('erikoisia',
        'ADJ'), ('näkökulmia', 'NOUN'), ('kaupunkiin', 'NOUN'), ('.',
        'PUNCT')], [('Vähän', 'ADV'), ('samanlainen', 'ADJ'),
        ('tunne', 'NOUN'), ('kuin', 'SCONJ'), ...] ... ]

        Don't change anything here.
        """
        tagged_sents = []
        try:
            # When we open a file with "with", the file is always cleanly closed as well
            with open(self.__filepath, "r", encoding="UTF-8") as gs_file:
                line = gs_file.readline()
                while line != "":
                    tagged_sents.append([nltk.tag.str2tuple(wt) for wt in line.split()])
                    line = gs_file.readline()
        except OSError:
            print("Error reading file.")
            sys.exit()
        return tagged_sents


    def read_sents(self):
        """ This method needs to read the file at self.__filepath and extract
        all the sentences from the file. The return value of this
        method should consist of a list of lists. On the highest
        level, we have a list of sentences. Then, every sentence
        consists of a list of word tokens. There *should be no POS tags
        included*, so make sure you remove them. Remember to handle exceptions
        caused by errors in reading files from disk.

        Example snippet of the data structure to return:
        [['Kävelyreitti', 'III'], ['Jäällä', 'kävely', 'avaa', 'aina',
        'hauskoja', 'ja', 'erikoisia', 'näkökulmia', 'kaupunkiin',
        '.'], ['Vähän', 'samanlainen', 'tunne', 'kuin', ... ] ... ]
        """
        sents = []
        
        try:
            with open(self.__filepath, "r", encoding="UTF-8") as f:
                lines = f.readlines()
                lines_split = []
                for line in lines:
                    line = line.rstrip("\n")
                    line = re.split(r'\/[A-Z]{1,5}\s*', line)
                    sents.append(line[:-1])
        except OSError:
                print("Error reading file.")
                sys.exit()

        return sents


    def tag(self):
        """ Tag the text using your regexp tagger and print out the tagged
        sentences. The tagger never sees the correct tags here.

        Don't change anything here.
        """
        for sent in self.read_sents():
            print(' '.join("{:s}/{:s}".format(word, tag)
                           for word, tag in self.__regexp_tagger.tag(sent)))

    def evaluate(self):
        """ Evaluate the regexp tagger on the text that contains the correct
        tags. That is, first the regexp tagger is applied to the data
        without looking at the correct answer. Then, the proposed tags
        are compared to the correct answer and the accuracy obtained
        is reported.

        Don't change anything here.
        """
        print("Accuracy:", self.__regexp_tagger.evaluate(self.read_tagged_sents()))


def main():
    """ Main method

    Don't change anything here.
    """
    tagger = FinnishRegexpPosTagger('fi-ud-train-3289.pos-tagged.txt')
    tagger.tag()
    tagger.evaluate()

main()
