
# Alias, by using =& the new variable you use will change if you change the olc variable. If you change the new variable it will also change.
#

<?php
/* Imagine a lot of code here */  
  $very_bad_unclear_name = "15 chicken wings";
  $order =& $very_bad_unclear_name;
// Write your code here:
 $order .= " Chicken";
  
  echo "\nYour order is: $very_bad_unclear_name.";