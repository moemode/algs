package StringMingler.src;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class StringMinglerTest {

    @Test
    public void testMingleStrings_case1() {
        String p1 = "abcde";
        String q1 = "pqrst";
        String expected1 = "apbqcrdset";
        String actual1 = StringMingler.mingleStrings(p1, q1);
        assertEquals(expected1, actual1);
    }

    @Test
    public void testMingleStrings_case2() {
        String p2 = "hacker";
        String q2 = "ranker";
        String expected2 = "hraacnkkeerr";
        String actual2 = StringMingler.mingleStrings(p2, q2);
        assertEquals(expected2, actual2);
    }
}
