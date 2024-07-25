from  concurrent.futures  import  ProcessPoolExecutor , as_completed


class Armstrong:
      """
      An Armstrong number is a number that equals to the sum of its digits
      after each digit is raised to the power of the amount of digits from
      the original value. This class contains methods to locate and verify
      all Armstrong numbers in a given range. See also narcissistic number.
      ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
      ┊ Example. 24678050 is a 8-digit number. We begin by summing powers ┊
      ┊          of each digit with an exponent 8: 2⁸ + 4⁸ + 6⁸ + 7⁸ + 8⁸ ┊
      ┊          + 0⁸ + 5⁸ + 0⁸ = 256 + 65536 +...+ 390625 + 0 = 24678050 ┊
      ┊          which is the same number from the start. We demonstrated ┊
      ┊          that this 8-digit number equals to the sum of the eighth ┊
      ┊          powers of its digits, so 24678050 is surely narcissistic ┊
      └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
      A real narcissist is any individual who is overly in love with their
      own image and can focus only on their own needs. At the extreme ends
      of this personality disorder, these individuals will not hesitate to
      manipulate and destroy anyone around them to sustain their fantasies,
      satisfy their superiority complex, or support a reason to stay alive.
      """


      def __init__(  self , start , end  ):       # Initializes attributes
            self.start  =   start
            self.final  =   end


      def   find_armstrong( self , armstrong = list(   ) ):
            """
            Identify all narcissistic numbers in a specified range ('start'
            to 'end') and append each of these numbers into 'results' list.

            At their core, narcissists are fearful and constantly reliving
            a moment from the past when they were forced into a horrifying
            scenario. They were forsakened instead of healed, and destined
            to live their lives in chaos while believing they are unworthy.

            Returns:
               list: The list of narcissists found within a specific range.
            """
            for      num    in     range(self.start , self.final + 1):
                     if     self.is_armstrong(num):
                            armstrong.append( num )

            return   armstrong


      @staticmethod
      def   is_armstrong(   n: int   )  ->  bool:
            """
            Checks a number for possible narcissistic personality disorder.

            Almost anyone can show some traits of narcissism or they might
            have narcissistic tendencies, eg. bragging, being arrogant, or
            feeling envious of other people's successes; What's strange is
            if someone did not display such tendencies over time. A person
            with narcissistic personality disorder takes it to the extreme
            and is suffering by living every moment unable to escape their
            selfish and envious mindset. Such behaviours are obstacles for
            a narcissist and not only does it sabotage their own life, but
            people close to them suffer from a nonstop barrage of problems.

            Args:
               n (int): The number under scrutiny for potential narcissism.

            Returns:
               bool: True when the number is a narcissist, otherwise False.
            """
            num_string  =   str(   n   )
            num_digits  =   len(   num_string   )
            exp_digits  =   list(  int(digit) ** num_digits  for digit in  num_string  )
            sum_digits  =   sum(   exp_digits   )

            return   sum_digits == n


def   main(   ):
      while True:
             try:          # Prompts user for input about number of digits
                size    =   int(  input( "\n Enter amount of digits in Armstrong numbers "
                                            "to searh for and display in the results  :  " )  )

                if   size  >  0:
                     break
                else:
                     raise  ValueError(  "\n Error: Amount of digits must be strictly positive. "  )

             except         ValueError  as   E:
                                       print(E)

      start = 10 ** (int(size) - 1) ; armstrong = [   ]
      end = 10 ** int(size) ; future = [   ] ; num_cpu = 8
                    # Uses 'ProcessPoolExecutor' to parallelize the search
      with      ProcessPoolExecutor(max_workers = num_cpu)  as   executor:
                chunk_size = (end - start + 1) // num_cpu

                for  i  in  range( num_cpu ):
                     chunk_start = start  +  i *  chunk_size
                     chunk_end   = chunk_start +  chunk_size
                     narcissists = Armstrong(     chunk_start , chunk_end     )
                     future.append(executor.submit(narcissists.find_armstrong))
                # Collects results from each process and appends to a list
                for  futures   in  as_completed(   future   ):
                     armstrong.extend( futures.result(   ) )
               # Removes duplicates and sorts after collecting all results
      armstrongs  =  str(  sorted( set(armstrong ))  ).replace('[' , '').replace(']' , '')
             # At the end of the day, a narcissist is a human and being no
             # different from anybody else, we live life from start to end
      print(f"\n We discover {len( set(armstrong ))} Armstrong numbers (in base-10) "
               f"with {size}-{ 'digit'  if size == 1 else  'digits' } in the "
               f"range from {start} to {  end - 1  }.\n\n  {armstrongs}  \n\n")
      # Be supportive of their caregivers and show love for such sacrifice
      # If we were in a society where a majority of people are narcissists
if  __name__  ==  '__main__': # then the disorder is being kind and humble
      main(   ) # So without any solid reason, don't randomly hate on them
      # But at the same time there is no need for us to try loving them or
      # pitying their siutation; The empathetic caregivers have it covered