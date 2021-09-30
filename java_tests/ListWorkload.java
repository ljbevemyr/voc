package voc;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Collectors;

import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;
import org.python.types.List;

public class ListWorkload {
    @Test
    public void testIsHashable() {
        assertEquals(false, false);
    }

    @Test
    public void addToList() {
        List test = new List();
        for (int i=0; i < 100000; i++) {
            test.append(org.python.types.Int.getInt(i));
        }
        for (int i=0; i < 250000; i++) {
            test.insert(org.python.types.Int.getInt(i), org.python.types.Int.getInt(i));
        }
        for (int i=0; i < 100000; i++) {
            test.remove(org.python.types.Int.getInt(i));
        }
    }
}
