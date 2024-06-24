// TODO: Tidy this up a bit. It works but its not pretty
import java.util.HashMap;
import java.util.ArrayList;

public class Main {
  public static void lookup(Character specialCharacter) {
    // Create the mapping of tokens and lexeme
    HashMap<Character, String> tokenMap = new HashMap<Character, String>();
    tokenMap.put('=', "20");
    tokenMap.put('+', "21");
    tokenMap.put('-', "22");
    tokenMap.put('*', "23");
    tokenMap.put('/', "24");
    tokenMap.put('(', "25");
    tokenMap.put(')', "26");
    tokenMap.put(';', "27");
    tokenMap.put(',', "28");
    if (tokenMap.containsKey(specialCharacter)) {
      System.out.println("Token is: " + tokenMap.get(specialCharacter) + " Lexeme is: " + specialCharacter);
    } else {
      System.out.println("Invalid lexeme: " + specialCharacter);
    }
  }

  public static String toString(ArrayList<Character> lexemeArray) {
    StringBuilder sb = new StringBuilder();
    for (Character c : lexemeArray) {
      sb.append(c);
    }
    return sb.toString();
  }

  public static Boolean isWhitespace(Character c) {
    return Character.isWhitespace(c);
  }

  public static void main(String[] args) {
    // reserved keyword
    String RESERVED_WORD = "int";

    // collect user input
    String userInput = System.console().readLine();
    // create ArrayList to hold the lexemes as they are parsed
    ArrayList<Character> lexemeArray = new ArrayList<>();

    // iterate over user input
    int i = 0;
    while (i < userInput.length()) {
      if (isWhitespace(userInput.charAt(i))) {
        i++;
        continue;
      }
      char c = userInput.charAt(i);
      int j = i;
      // letters (identifier) is token code 11
      if (Character.isLetter(c)) {
        while (j < userInput.length() && !isWhitespace(userInput.charAt(j)) && Character.isLetter(userInput.charAt(j))) {
          lexemeArray.add(userInput.charAt(j++));
        }
        // Check if lexeme is reserved
        if (RESERVED_WORD.equals(toString(lexemeArray))) {
          // RESERVED token code 12
          System.out.println("Token is: 12 " + "Lexeme is: " + toString(lexemeArray));
        } else {
          // identifier code 11
          System.out.println("Token is: 11 " + "Lexeme is: " + toString(lexemeArray));
        }
        // set I to J location to avoid iterating over characters twice
        i = j;
        // clear the lexeme array and start fresh
        lexemeArray.clear();
        // INT_LIT is token code 10
      } else if (Character.isDigit(c)) {
        while (j < userInput.length() && !isWhitespace(userInput.charAt(j)) && Character.isDigit(userInput.charAt(j))) {
          lexemeArray.add(userInput.charAt(j++));
        }
        System.out.println("Token is: 10 " + "Lexeme is: " + toString(lexemeArray));
        i = j;
        lexemeArray.clear();
      } else if (!isWhitespace(c)) {
        lookup(c);
        i++;
      }
    }
  }
}
