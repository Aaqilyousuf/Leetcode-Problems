import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> map = new HashMap<>();

        // Count characters from `s` and `t`
        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            map.put(c1, map.getOrDefault(c1, 0) + 1);
            map.put(c2, map.getOrDefault(c2, 0) - 1);
        }

        // Check if all counts are zero
        for (int count : map.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}
// import java.util.HashMap;

// class Solution {
//     public boolean isAnagram(String s, String t) {
//         if (s.length() != t.length()) {
//             return false;
//         }

//         HashMap<Character, Integer> map1 = new HashMap<>();
//         HashMap<Character, Integer> map2 = new HashMap<>();

//         // Count character frequencies for `s`
//         for (char c : s.toCharArray()) {
//             map1.put(c, map1.getOrDefault(c, 0) + 1);
//         }

//         // Count character frequencies for `t`
//         for (char c : t.toCharArray()) {
//             map2.put(c, map2.getOrDefault(c, 0) + 1);
//         }

//         // Compare the two maps
//         return map1.equals(map2);
//     }
// }

