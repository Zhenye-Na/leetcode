class MyCalendar {

    private TreeMap<Integer, Integer> calendar;

    public MyCalendar() {
        calendar = new TreeMap<>();
    }

    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start);
        Integer next = calendar.ceilingKey(start);

        if (prev != null && calendar.get(prev) > start) {
            return false;
        }

        if (next != null && next < end) {
            return false;
        }

        calendar.put(start, end);
        return true;
    }
}
