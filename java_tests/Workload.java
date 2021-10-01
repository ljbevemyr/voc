package voc;

import org.junit.Test;
import org.python.exceptions.AttributeError;
import org.python.exceptions.KeyError;
import org.python.exceptions.TypeError;
import org.python.types.*;
import org.python.types.List;
import org.python.types.Object;
import org.python.types.Set;

import java.util.*;
import java.util.ArrayList;
import java.util.Map;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.*;

public class Workload {
    public static void workloadUpdate() {
        Map<org.python.Object, org.python.Object> emptyMap = new HashMap<>();
        Dict kwargsDict = new Dict(emptyMap);

        Str a = new Str("aasdfasdfasdfsadf");
        Str b = new Str("basdfasdfasdfasdfa");
        Str c = new Str("basdfasdf232432asdfasdfa");
        Str d = new Str("basdfasd234234fasdfasdfa");
        Str e = new Str("bas234234dfasdfasdfasdfa");
        Str f = new Str("basdfasdfasdfasdfa");
        Str g = new Str("basdfas234234dfasdfasdfa");
        Str h = new Str("bas23234dfasdfasdfasdfa");
        Str i = new Str("basdfasdf234234asdfasdfa");
        Str j = new Str("basdfas234234dfasdfasdfa");
        Int one = Int.getInt(1);
        Int two = Int.getInt(2);
        Int three = Int.getInt(3);
        Int four = Int.getInt(4);
        Int five = Int.getInt(5);
        Int six = Int.getInt(6);
        Int seven = Int.getInt(7);
        Int eight = Int.getInt(8);
        Int nine = Int.getInt(9);
        Int ten = Int.getInt(10);
        Map<org.python.Object, org.python.Object> kwargsMap1 = new HashMap<>();
        kwargsMap1.put(a, one);
        kwargsMap1.put(b, two);
        kwargsMap1.put(c, three);
        kwargsMap1.put(d, four);
        kwargsMap1.put(e, five);
        kwargsMap1.put(f, six);
        kwargsMap1.put(g, seven);
        kwargsMap1.put(h, eight);
        kwargsMap1.put(i, nine);
        kwargsMap1.put(j, ten);
        Dict kwargsDictInput1 = new Dict(kwargsMap1);

        Str a1 = new Str("aasdfasdfasdfsadf");
        Str b1 = new Str("basdfasdfasdfasdfa");
        Str c1 = new Str("basdfasdf232432asdfasdfa");
        Str d1 = new Str("basdfasd234234fasdfasdfa");
        Str e1 = new Str("bas234234dfasdfasdfasdfa");
        Str f1 = new Str("basdfasdfasdfasdfa");
        Str g1 = new Str("basdfas234234dfasdfasdfa");
        Str h1 = new Str("bas23234dfasdfasdfasdfa");
        Str i1 = new Str("basdfasdf234234asdfasdfa");
        Str j1 = new Str("basdfas234234dfasdfasdfa");
        Int one1 = Int.getInt(1);
        Int two1 = Int.getInt(2);
        Int three1 = Int.getInt(3);
        Int four1 = Int.getInt(4);
        Int five1 = Int.getInt(5);
        Int six1 = Int.getInt(6);
        Int seven1 = Int.getInt(7);
        Int eight1 = Int.getInt(8);
        Int nine1 = Int.getInt(9);
        Int ten1 = Int.getInt(10);
        Map<org.python.Object, org.python.Object> kwargsMap2 = new HashMap<>();
        kwargsMap2.put(a1, one1);
        kwargsMap2.put(b1, two1);
        kwargsMap2.put(c1, three1);
        kwargsMap2.put(d1, four1);
        kwargsMap2.put(e1, five1);
        kwargsMap2.put(f1, six1);
        kwargsMap2.put(g1, seven1);
        kwargsMap2.put(h1, eight1);
        kwargsMap2.put(i1, nine1);
        kwargsMap2.put(j1, ten1);
        Dict kwargsDictInput2 = new Dict(kwargsMap2);

        for (int index = 0; index < 1000; index++) {
            kwargsDict.update(null, kwargsDictInput1);
            kwargsDict.update(null, kwargsDictInput2);
        }
    }

    public static void main(String[] args) {

        System.out.println("Running workload...");
        workloadUpdate();
        System.out.println("Done");

    }
}
