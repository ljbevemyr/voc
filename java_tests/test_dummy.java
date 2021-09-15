import org.junit.jupiter.api.Test;
import org.python.stdlib.datetime.Date;
import org.python.stdlib.datetime.DateTime;

import java.util.Collections;

import static org.junit.jupiter.api.Assertions.assertEquals;


class DummyTest {

    @Test
    public void testInitilize() {
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(30)};
        Date date = new Date(args, Collections.emptyMap());
        assertEquals(new org.python.types.Str("30"), date.__day__());
        assertEquals(new org.python.types.Str("9"), date.__month__());
        assertEquals(new org.python.types.Str("2021"), date.__year__());
    }

    @Test
    public void testToday() {
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(30)};
        Date date = new Date(args, Collections.emptyMap());
        System.out.println(date);
        assertEquals(new org.python.types.Str("2021-09-15"), date.today().__repr__());
    }

    @Test
    public void testctime() {
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(15)};
        Date date = new Date(args, Collections.emptyMap());
        System.out.println(date);
        assertEquals(new org.python.types.Str("Wed Sep  15 00:00:00 2021"), date.ctime());
    }

    @Test
    public void testweekday() {
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(15)};
        Date date = new Date(args, Collections.emptyMap());
        System.out.println(date);
        assertEquals(2, new Integer(String.valueOf(date.weekday())));
    }
}
