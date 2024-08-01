from  multiprocessing  import  Process , Queue
from  textwrap         import  fill


class Memo:
      """
      Applies singleton method as a data collection tool.
      """

      _instance  =   None                # Stores the single instance of the class
      data       =   dict(   )                # Stores data for the class instance


      def __new__(   cls  ,  *args  ,  **kwargs   ):
            if  not  cls._instance:                  # Class instance is not found
                     cls._instance = super(   ).__new__(cls)   # Create superclass

            return   cls._instance           # Return single instance of the class


class My_Happiness:
      """
      Some numbers are able to understand basic emotions.
      If a number is positive and wholesome, then it can
      experience the emotion of happiness and be content.
      Otherwise, if a number is negative and pretentious,
      it is destined to be gloomy and miserable. The two
      words 'positive' and 'negative' are used for their
      psychological context only and have no relation to
      a mathematical sense of whether a value is below 0.

      A happy number is defined by the following process:
      - Starting with some positive integer, replace the
        number with the sum of the squares of its digits
      - Repeat process until the sum turns into a '1' or
        process repeats a cycle that '1' isn't a part of
      - If the number eventually becomes '1', then label
        it as a happy number; otherwise we say it is sad

      Methods:
      - in_memory:        Optimizes runtime complexity.
      - feels_happy:       Validates the emotional state.
      - the_lighthouse: Identifies spectrum of happiness.
      """


      def   in_memory(    self , n: int , memo: dict    )  ->  bool:
            """
            Any permutation of the digits in a happy number gives another happy number.
            The same can be said for the digits that form sad numbers. Rearranging the
            digits into a different number will not take away the emotion of being sad.
            If 'n' knew happiness in the past, then happiness awaits 'n' in its future.

            This method accounts for the invariance of happy numbers through recording
            the frequency of non-zero digits of 'n' inside 'tally' before storing this
            count into a cache under its 'happy' category. If some new number is being
            investigated for happiness and the number's digits count is an exact match
            with some data from the cache's 'happy' category, then we will immediately
            know the number belongs with happiness. Similarly, happiness is deduced in
            other values throughout the investigation upon the discovery of statistics
            as pre-existent in the cache. The memoization technique is applied here to
            avoid any resulting redundancies when permuting a set of objects on itself.

            There are only two 'on-buttons' for fear, in any permutation you want. One
            button is when something that shouldn't be — is, eg. a presence. The other
            one is an absence. I fear quite a lot of what I do not understand and what
            I still do not understand is the notion of love. It is not just an emotion.

            Args:
               n (int):              The number to investigate for potential happiness.
               memo (dict):                  A cache with data from known happy values.

            Returns:
               bool:              True when a number is happy and False when it is sad.
            """
            tally    =    [   ]        # Creates an empty list for tallying digits
            n_str    =    str(n).replace('0' , '')  # Remove 0s with str 'replace'

            for   i  in   range(  1 , 10  ):
                  i  =    str(i)      # Converts 'i' to a str type for str 'count'

                  if i     in     n_str:     # Tallies frequency of nonzero digits
                     tally.append((  i , n_str.count(i)  )) # Stores data in tuple

            if    tally   in      memo[ 'happy' ]:
                  return  True     # 'n' inherits its happiness from the ancestors
            elif  tally   not in  memo[ 'happy' ]    and    self.feels_happy(n):
                  memo[  'happy'  ].append(tally) # Cache aquires brand new member
                  return  True                 # 'n' is recognized for being happy
            else:               # None of the given conditions are fitting for 'n'
                  return  False     # 'n' is discarded for failing to become happy


      def   feels_happy(  self , n: int  )  ->  bool:
            """
            Applies the algorithm on 'n' to determine its emotional state.
            A sequence of terms is produced in each step of the algorithm
            and by analyzing each term in the resulting sequence from 'n',
            we can determine with absolute certainty which emotion 'n' is
            experiencing, the series of transforms that lead to the onset
            of either emotion, and time duration before 'n' is self-aware.

            When you truly care for someone, their feelings and wellbeing
            become intertwined with your own. You can't find happiness or
            joy knowing your actions have cause them pain. If you realize
            that someone you care about is suffering because of something
            you did or said to them, it creates a disconnect in you. Real
            love with genuine care involves empathy and sharing emotional
            experiences. Hurting a person you care about affects your own
            sense of worth. Inflicting pain and suffering on another is a
            clear indication that the bond lacks joy, and will ultimately
            lead to a harvest of resentment and a life filled with sorrow.

            How do we identify true happiness, contentment, or joyfulness?
            When can we be certain it's not just a facade? Happiness is a
            positive emotional state triggered by external factors. It is
            a fixated emotion, a temporary encounter, and merely a result
            from a reaction. Knowing if someone is feeling happy is quite
            straightforward, as the effects of happiness are very obvious
            in a person's demeanour. The challenge lies in our ability to
            discern whether this happiness leads to genuine joy, or if it
            is simply a clever disguise for hiding selfish personal gains.

            Args:
               n (int): The number to investigate for potential happiness.

            Returns:
               bool: True when a number is happy and False when it is sad.
            """
            seen  =  set(   )  # Stores transformations (or sequence terms) of 'n'
            while    n != 1:          
                     if   n   in  seen:    # 'n' reverts into a previous transform
                          return  False    # Lack of happiness triggered a relapse

                     seen.add(n)     # Tracks all forms of 'n' seen its past lives
                     n  = sum(int(digit) ** 2    for digit in    str(n))

            return   True         # 'n' escapes loop and is finally becoming happy


      def   the_lighthouse( self , start: int , end: int , memo: dict , queue: Queue)  ->  None:
            """
            Identifies a range of happy numbers before storing into Queue.
            This method is dependent on 'in_memory' to verify every happy
            number in a range from 'start' to 'end'. If the value's stats
            are found inside cache, 'n' will instantly be classified as a
            happy number. Otherwise, 'n' is checked against the algorithm.

            Being content is more sustainable and a clear preference over
            being in a state of happiness. Having a consistent mindset, a
            continual yearning to foster inner balance, and an unstopable
            focus towards making self-improvements; is how abundant bliss
            is unlocked in life. To be with the company of contentment is
            to have a powerful ally if you ever wrestle against adversity.

            Joy is found only when we purposely go looking for it. Search
            with relentless effort, fiery-like desire, unwavering resolve;
            for Joy is what keeps us free. May Joy's glorious presence be
            found within you and always be surrounding you. How wonderful
            it is to rejoice in pleasures and to see beyond the suffering.
            On the journey to find Eternal joy, we learn to overcome pain.
            Pain is inevitable but we must endure since Joy is the reward.

            Args:
               start (int):         Indicator for the beginning of search.
               end (int):         Index (exclusive) for ending the search.
               memo (dict):     Cache storing data of known happy numbers.
               queue (Queue): FIFO storage for interprocess communication.
            """
            happy_numbers = list(   )        # Creates an empty list for happiness

            for  n   in     range( start , end ):
                 if  self.in_memory( n , memo ):
                     happy_numbers.append( n )                  # Adds 'n' to list
                     continue

            queue.put(      happy_numbers      )            # Puts list in 'queue'


class Really_Wanna:
      """
        ╒═════════════╦═══════════════════════════════════════════════╦
        ╎             ║     If you want my future, forget my past     ║
        ╽             ║ If you wanna get with me, better make it fast ║
        ╏             ╫┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄             ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╫
        ╿ Soo tell me what you want┈┈┈. ˙  ˙·   ·˙  ˙ .┈┈┈what u really really want ┋
        ┆ I'll tell you what I want┈┈.        ˙        .┈┈what I really really want ╿
        ╽     ❤️💟❤️💝❤️💘        ·                 ·        ❤️💗❤️💖❤️💓     ┊
        ┇ If  u  wana  b  my  lover┈┈┈·               ·┈┈┈u gotta get wit ma fwends ╽
        ╿ Make   it  last   forever┈┈┈┈˙.           .˙┈┈┈┈fwendship    neva    ends ┇
        ┊     ❤️💗❤️💖❤️💓            ˙.       .˙            ❤️💟❤️💝❤️💘     ╿
        ╽ If  u  wana  b  my  lover┈┈┈┈┈┈┈┈˙.   .˙┈┈┈┈┈┈┈┈u   hav   got   to   give ┆
        ┋ Taking    is    2    easy┈┈┈┈┈┈┈┈┈┈˙.˙┈┈┈┈┈┈┈┈┈┈but  thats the way it  is ╽
                       ╫┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╫              ╏
                            Now don't go wasting my precious time                   ╿
                         Get your act together we could be just fine                ╎
                       ╩═════════════════════════════════════════════╩══════════════╛

      Methods:
      - zigzag:          Applies the step-by-step process from the happiness algorithm.
      """


      @staticmethod
      def   zigzag(  n: int  )  ->  list:
            """
            This class method will apply the happy algorithm on some integer 'n' until
            the occurence of a repeating loop in the sequence or the appearance of a 1.

            Tell me in all honesty, what is love? Oh baby don't hurt me, don't hurt me
            no more. Absence sharpens love while presence strengthens it. Perhaps love
            is the embodiment of both the candle and the wind simultaneously. When the
            candle is lit, the wind around its flame gets blurry. Why? Because science.
            So a candle must remain strong and burn brightly when it's confronted with
            gusts of wind, lest it chooses to extinguish and its flame become forsaken.

            Args:
               n (int):               The number to investigate for possible happiness.

            Returns:
               list:           The completed happy sequence with 'n' as the first term.
            """
            path  = [n]    # Creates a list for visualizing unique transformations

            while    n != 1:               # Sum of the squares from digits of 'n'
                     digit_sum =  sum(   int(  digit  ) ** 2    for  digit  in    str(n)   )

                     if   digit_sum  in  path:     # Sequence has a repeating loop
                          idx  =  path.index(  digit_sum  )  # Finds start of loop
                          return  path + path[ idx : idx + 9 ]  +  [ digit_sum ]
                     else:
                          path.append(   digit_sum  )     # Adds new sum to 'path'
                          n    =  digit_sum           # Grants 'n' a new transform

            return   path     # '1' appears so 'n' is happy and sequence is unique


class Always:
      """
      The writing is on the wall. There's nothing I could change or undo. But I will
      be there beside you when it rains, beside you when it storms, keeping you safe.
      So don't you ever lose your Faith. Trust that I will stay I'll Always be there.

      Methods:
      - rejoice:       Applies the step-by-step process from the happiness algorithm.
      """


      @staticmethod
      def   rejoice(     chunk_size: int , num_processes : int , memo:  dict     )  ->  list:
            """
            Finds happy numbers within a specified range using multiprocessing. Divides
            the workload among multiple processes to make runtime more efficient and to
            enhance the program's efficiency. Adjust 'chunk_size' based on size of each
            task and adjust 'num_processes' based on the required amount of parallelism.

            What if I'm like 'n', when it was unsure about his happiness and waiting on
            a verdict? What if I'm actually not happy? Even scarier, what if...I Am Love.

            Returns:
               list:      The sorted list of happy numbers from subprocess computations.
            """
            stronghold = My_Happiness(   )

            results_queue = Queue(   )  ;  processes = [   ]  ;  happy_numbers = [   ]

            for   i  in   range(  num_processes ):
                  chunk_start  =  i  *  chunk_size  +  1
                  chunk_end    =  chunk_size + chunk_start    if  i < num_processes - 1  else    chunk_size + chunk_end
                  num_process  =  Process( target = stronghold.the_lighthouse , args = ( chunk_start , chunk_end , memo , results_queue ) )
                  num_process.start(   )
                  processes.append(  num_process  )

                  for     process in     processes:
                          process.join(   )
                         # Collects results from all processes and appends to list
                  while   not     results_queue.empty(   ):
                          happy_numbers.extend(results_queue.get(   ))

            return   sorted(set(  happy_numbers  ))


class After:
      """
                              ╦═══════════════════════════════╦═════════════════════╕
                              ║ So here's a story from A to Z ║                     ╎
        ┊     ❤️💗❤️💖❤️💓 ╫┄┄┄┄┄┄┄┄┄             ┄┄┄┄┄┄┄┄┄╫ ❤️💟❤️💝❤️💘     ╽
        ╽ You  wanna  get  with  me┄┄┄. ˙  ˙·   ·˙  ˙ .┄┄┄u gotta listen  carefully ╏
        ┋                            .        ˙        .                            ╿
        ╿ We  got  M  in  da  place┄┄·                 ·┄┄who  likes  it in yo'face ┆
        ┊                             ·               ·                             ╽
        ╽ You   got   G   like   MC┄┄┄┄˙.           .˙┄┄┄┄who  likes  it   on   any ┇
        ┇                                ˙.       .˙                                ╿
        ╿ See,   V   doesn't   come┄┄┄┄┄┄┄┄˙.   .˙┄┄┄┄┄┄┄┄for free—shes a real lady ┊
        ┆     ❤️💗❤️💖❤️💓                ˙.˙                ❤️💟❤️💝❤️💘     ╽
        ╿                    ╫┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄╫
        ╎                      And as for me 🤫 You will See 
        ╘════════════════════╩═══════════════════════════════╩

      Methods:
      - glow:        Gives option to view happy sequences after they finish processing.
      """


      @staticmethod
      def   glow(     option: dict = {   }  ,  _message: dict = {   }     )   ->   None:
            """
            Verify potential joyfulness from a number using sequential transformations.
            All terms in a sequence produced from 'glow' follow the same exact pattern
            described in the happiness algorithm. When 'glow' method is first accessed,
            then the program is in its final stage and provides user a choice to leave.

            If you know someone is happy because your presence has that effect on them,
            then you also need to know that there is some form of Goodness within your
            spirits. In your shared moments of happiness, do you notice the vibrations
            flowing out from your souls? Putting a smile on somebody else's face while
            making them feel happy can change the world; Well, not the whole world but
            you are certainly changing their world. So cherish those moments and build
            a genuine connection if you're serious about wanting to improve your lives.

            Args:
               option   (dict): Key phrases used to determine which message to display.
               _message (dict):   Summary statements for each possible emotional state.
            """
            She   =   My_Happiness(   )  # comfort, home, pride, wanderer, warrior

            bld   =   '\033[1m'  ;  blu   =   '\033[34m'  ;  drkred   =   '\033[1;31m'  ;  red   =   '\033[31m'
            rst   =   '\033[0m'  ;  grn   =   '\033[33m'  ;  drkblu   =   '\033[1;34m'

            space =  {    k : ' ' * ( 9 - k )    for  k  in    range(1  ,  8)    }
            space.update({k : ' '    for  k  in    range(8  ,  99)})

            print(   "\n      You can verify potential happiness in a random number through invoking      "   )

            while    True:
                      try:
                          together   =   input(  f"      my {  red  }happy algorithm{  rst  }. Go ahead and try "
                                                 f"inputting the number with {    bld    }NUMKEYs{    rst    }: "  )

                          if      together  ==  '0'     or     'N'  in  together.upper(   ):
                                  print( f"\n\n{' '*24}👋 👋 👋     Bye     👋 👋 👋{' '*24}\n\n" )
                                  return
                          elif    together.isnumeric(   ):
                                  really_really     =   Really_Wanna.zigzag(  together  )
                                  your_choice       =   really_really[ -1 ]
                                  stay              =   len(really_really)
                                         # his Beloved can never truly be replaced
                                  if     She.feels_happy(      together      ):
                                         impossible =   ' ⟶ '.join(  map( str  ,  really_really[1 :   ]  +  ['✔️'] )  )
                                         our_bond   =   impossible.replace("'"     ,     "")
                                         lesson     =   fill(  our_bond , width = 66 , initial_indent = '' , subsequent_indent = ' ' * (15 + len(str(together)))  )
                                  else: # his replacement can never be truly loved
                                         bad_karma  =   ' ⟶ '.join(  map( str  ,  really_really[1 :   ]  +  ['...']  +  ['ꝏ'] )  )
                                         lifetime   =   bad_karma.replace( "'"    ,    "" )
                                         lesson     =   fill(  lifetime , width = 66 , initial_indent = '' , subsequent_indent = ' ' * (15 + len(str(together)))  )
                                           # loniless, like a heartbeat drives you
                                  _message.update({ 1      :   f"\n{' ' * 9}{ red }{together}{rst}: {       grn       }{lesson}{ rst }     \n" })
                                  _message.update({ 2      :   f"\n{' ' * 9}{ red }{together}{rst}  is  {   red   }très happy{   rst    } and"
                                                               f" discovers her {  drkred  }significant one{rst} after {bld}{   stay - 1   } "
                                                               f"{  rst  }attempt{  's '    if  stay != 2  else    ' '  }{       red       } "
                                                               f"{  ' ' * (5 - len(str(stay) + str(together)))  }💞 ♡⸜(˶˃ᵕ˂˶)⸝♡ 💕{rst} \n\n"
                                                                "      Are you thinking about a next value and does it seem happy to you? Use" })
                                  _message.update({ 3      :   f"\n{' ' * 9}{blu}({together}){rst}: { grn }{lesson}{         rst         } \n" })
                                  _message.update({ 4      :   f"\n{' ' * 9}{blu} {together}{ rst }   is  { blu }not happy{  rst  }—there is "
                                                               f"{drkblu}sadness and sorrow{ rst } from an 8-cycle on {bld}{your_choice}{rst}"
                                                               f"{  ' ' * ( 5 - len(str(your_choice) + str(together)) )  }   [\033[2;34mterm "
                                                               f"{           really_really.index(your_choice)           }{   rst   }]    \n\n"
                                                                "      Is there a next number on your mind? Is it genuine happiness? Remember" })
                               # mad, in the stillness of remembering what you had
                                  hash_tag   =    {     'the-rest-of-u'      :  1 ,
                                                        'quiet-treason'      :  3 ,
                                                        'or-nothing-at-all'  :  2 ,
                                                        'a-fortnight-there'  :  4 ,
                                                        }
                                  option.update(  {     words  :  _message[hash_tag[words]]    for words in    hash_tag.keys(   )     }  )
                                     # and what you had and what you lost; Thunder
                                  if     She.feels_happy(      together      ):
                                         print( option[ 'the-rest-of-u' ]   +   option[ 'or-nothing-at-all' ] )
                                  else:           # only happens when it's raining
                                         print( option[ 'quiet-treason' ]   +   option[ 'a-fortnight-there' ] )
                          elif    '-' in together:
                                  raise  ValueError(f"\n        Error:  Each term in a {   red   }happy progression{  rst  } must be strictly "
                                                     "positive.\n\n      What is the correct value? How likely is it to reveal happiness? Apply")
                          elif    '.' in together   or   '/' in together:
                                  raise  ValueError(f"\n        Error:  The terms within {   red   }happy sequences{  rst  } can only be whole "
                                                     "numbers.\n\n      What is the correct value? How likely is it to reveal happiness? Apply ")
                          else:
                                  raise  TypeError( f"\n        Error:  Every term in {  red  }happy sequences{  rst } contain numeral symbols "
                                                     "only.\n\n      What is the correct value? How likely is it to reveal happiness? Apply    " )

                      except      ValueError   as   Players:  # only love you when
                                           print(   Players  )
                      except      TypeError    as   they:       # 're playing; Say
                                           print(   they   )


def   main(   ):
      print( f"\n{' ' * 16} \033[32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
              "\n      🎵  \033[32m 💃    ┫ We Found Love in \033[1mA"
              " Happy Place \033[0;32m┣    🎼 \033[0m  🎶          \n"
             f"{' '  * 15}  \033[32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" )

      processes        =  125             # women, they will come and they will go
      chunks           =  8000       # when the rain washes you clean, you'll know
      num_range        =  processes * chunks

      memo             =  Memo(   ).data                    # You ## Will ### Know
      memo.update(  {     'happy'   :   [   ]     }  )

      happy_numbers    =  Always.rejoice( chunks , processes , memo )

      results          =  ', '.join( map( str  ,  happy_numbers ) )
      _message         =  fill( results , width = 83 , initial_indent = ' ' * 9 , subsequent_indent = ' ' * 9 )

      total            =  len(   happy_numbers   )
      actual           =  round( total / num_range * 100  , 2 )
      margin           =  round((actual    -    15)    *    100)

      bld = '\033[1m'  ;  grn = '\033[32m' ; shd = '\033[2;47m' ; itlblu = '\033[2;3;34m' ; rst    = '\033[0m'
      itl = '\033[3m'  ;  red = '\033[31m' ; ltgrn = '\033[33m' ; bkgltgrn = '\033[2;43m' ; bkggrn = '\033[2;42m'

      outcome = {    1 :  '0'    if str(actual)[ -2 ] == '.' else    '' ,
                     2 :  'loss'    if margin < 0 else    'gain'        ,    }
      space   = {    k :  ' ' * (16 - k)    for  k  in    range(2  ,  16)    }
      space.update({ k :  ''    for  k  in    range(16  ,  99) })

      print( f"\n{   ' ' * 9   }{ bld }{  itl  }Def{rst}.    A {red}Happy Number{rst} "
             f"is a number which will eventually reach {     bld     }1{  rst  } after"
             f"\n{   ' '  *  17   }successive replacement by the sum of the squares of"
             f" its digits.\n\n{   ' '  *  9   }{  bld  }{  itl  }Ex{     rst     }.\n"
              "                        77777777  ⟶   7² + 7² +...+ 7²   =  392     \n"
              "                             392  ⟶     3² + 9² + 2²     =  94      \n"
              "                              94  ⟶       9² + 4²        =  97      \n"
              "                              97  ⟶       9² + 9²        =  130     \n"
              "                             130  ⟶     1² + 3² + 0²     =  10      \n"
              "                              10  ⟶       1² + 0²        =  1\n\n   \n"
              "                             😵 😖 😯 😭 😢 😌 😓 😰 😟 😞 🥺 \n\n" )
      print(           _message           )
      print( f"\n      Among all integers from \033[2m1{rst} to \033[2m{  num_range  }"
             f"{   rst   }, {     shd     }{  total  }{ rst } experience happiness. \n"
             f"\n         ◾ {     ltgrn     }natural density{      rst      } in base-"
             f"10 is approximately {   bkgltgrn   }15.00%{         rst         }      "
             f"\n         ◾ current estimate for the { grn }happiness ratio{ rst } is "
             f"{   bkggrn   }{  actual  }{       outcome[1]       }%{     rst     } \n"
             f"\n         We are observing a {   outcome[2]   } of {shd} {abs(margin)}"
             f"  { rst } pips on {    red    }global/local happiness{     rst     }.\n" )
              # I dream alone under the moon. It is brighter when you are with me.
      print( f"{ ' '  * 10  }\033[34m┌──────────────────────────────┐{    rst    }  \n"
             f"    {itlblu}📕{' ' * 4}┤ A Series of {bld}Fortunate Events{rst}\033[34m"
             f" ├ { rst }   📚   Press \033[1;46m 0 {rst} anytime to {bld}QUIT{rst} \n"
             f"{ ' '  * 10  }\033[34m└──────────────────────────────┘{    rst    }  \n" )

      After.glow(   ) # is strong enough to light this fire. This fire back in us.

      quit(   )


if  __name__   ==   '__main__':
      main(   )