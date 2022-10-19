public class TinyLife {

    public static void main(String[] args) throws Exception {
        Long world = Long.decode(args[0]);
        print(world);
        Long updated_world = setCell(world, 1, 1, true );
        print(updated_world);
    }

    public static boolean getCell(long world, int col, int row) {
        boolean grid_check = (col > 7) | (col < 0) | (row > 7) | (row < 0);
        return grid_check;
    }

    public static long setCell(long world, int col, int row, boolean value) {
        int place = (col * 7) + (col + row);
        long updated_world = PackedLong.set(world, place, value);
        return updated_world;
    }

    public static void print(long world) {
        System.out.println("-");
        for (int row = 0; row < 8; row++) {
            for (int col = 0; col < 8; col++) {
                System.out.print(getCell(world, col, row) ? "#" : "_");
            }
            System.out.println();
        }
    }


}
