public class TinyLife {

    public static void main(String[] args) throws Exception {
        play(Long.decode(args[0]));
    }

    public static boolean getCell(long world, int col, int row) {
        boolean grid_check = (col > 7) | (col < 0) | (row > 7) | (row < 0);
        return grid_check;
    }

    public static long setCell(long world, int col, int row, boolean value) {
        int point = col + (row * 8);
        long updated_world = PackedLong.set(world, point, value);
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


    public static int countNeighbours(long world, int col, int row) {
        int neighbours = 0;
        //the ? replaces the if, they mean the same thing except that using ? allows u to do it in 1 line
        neighbours += (getCell(world, col-1, row-1)) ? 1: 0;
        neighbours += (getCell(world, col, row-1)) ? 1: 0;
        neighbours += (getCell(world, col+1, row-1)) ? 1: 0;
        neighbours += (getCell(world, col-1, row)) ? 1: 0;
        neighbours += (getCell(world, col+1, row)) ? 1: 0;
        neighbours += (getCell(world, col-1, row+1)) ? 1: 0;
        neighbours += (getCell(world, col, row+1)) ? 1: 0;
        neighbours += (getCell(world, col+1, row+1)) ? 1: 0;
        return neighbours;
    }

    public static boolean computeCell(long world,int col, int row){
        boolean liveCell = getCell(world, col, row);
        int neighbours = countNeighbours(world, col, row);
        boolean nextCell = false;
        if (neighbours < 2) {
            nextCell = false;
        }
        if (liveCell && neighbours == 2 || liveCell && neighbours == 3) {
            nextCell = true;
        }
        if (neighbours > 3) {
            nextCell = false;
        }
        if (!liveCell && neighbours == 3) {
            nextCell = true;
        }
        return nextCell;
    }

    public static long nextGeneration(long world){

    }

    public static void play(long world) throws Exception {
        int userResponse = 0;
        while (userResponse != 'q'){
            print(world);
            userResponse = System.in.read();
            world = nextGeneration(world);
        }
    }
}


