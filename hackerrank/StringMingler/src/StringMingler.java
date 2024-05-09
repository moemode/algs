package StringMingler.src;

public class StringMingler {

    /**
     * Mingles two strings of equal length into a new string following the pattern:
     * For strings P = p1p2p3...pn and Q = q1q2q3...qn, the mingled string is:
     * p1q1p2q2p3q3...pnqn
     *
     * @param p The first string (Pawel's favorite).
     * @param q The second string (Shaka's favorite).
     * @return The mingled string as per the specified pattern.
     */
    public static String mingleStrings(String p, String q) {
        // Implement mingling logic here
        // This method should return the mingled string based on the input strings p and
        // q
        // Example:
        // For input strings p = "abcde" and q = "pqrst", the output should be
        // "apbqcrdset"

        // Placeholder return, replace with actual logic
        StringBuilder mingled = new StringBuilder(2 * p.length());
        for (int i = 0; i < p.length(); i++) {
            mingled.append(p.charAt(i));
            mingled.append(q.charAt(i));
        }
        return mingled.toString();
    }
}