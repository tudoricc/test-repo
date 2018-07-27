private static int computeNextNumber(int number) {
		if (number == 1)
			return 1;

		int[][] matrix = new int[960][960];
		matrix[480][480] = 1;

		int i = 480;
		int j = 480;
		int step = 1;
		boolean finalStep = false;

		while (true) {
			// Move right
			for (int k = 0; k < step; k++) {
				matrix[i][++j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
						+ matrix[i + 1][j + 1] + matrix[i + 1][j - 1] + matrix[i - 1][j + 1] + matrix[i - 1][j - 1];

				if (finalStep == true)
					return matrix[i][j];
				if (matrix[i][j] > number)
					return matrix[i][j];
				if (matrix[i][j] == number)
					finalStep = true;
			}

			// Move up
			for (int k = 0; k < step; k++) {
				maxRegName = new String(regName);
				matrix[--i][j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
						+ matrix[i + 1][j + 1] + matrix[i + 1][j - 1] + matrix[i - 1][j + 1] + matrix[i - 1][j - 1];

				if (finalStep == true)
					return matrix[i][j];
				if (matrix[i][j] > number)
					return matrix[i][j];
				if (matrix[i][j] == number)
					finalStep = true;
			}

			step++;
			// Move left
			for (int k = 0; k < step; k++) {
				matrix[i][--j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
						+ matrix[i + 1][j + 1] + matrix[i + 1][j - 1] + matrix[i - 1][j + 1] + matrix[i - 1][j - 1];

				if (finalStep == true)
					return matrix[i][j];
				if (matrix[i][j] > number)
					return matrix[i][j];
				if (matrix[i][j] == number)
					finalStep = true;
			}

			// Move down
			for (int k = 0; k < step; k++) {
				matrix[++i][j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
						+ matrix[i + 1][j + 1] + matrix[i + 1][j - 1] + matrix[i - 1][j + 1] + matrix[i - 1][j - 1];

				if (finalStep == true)
					return matrix[i][j];
				if (matrix[i][j] > number)
					return matrix[i][j];
				if (matrix[i][j] == number)
					finalStep = true;
			}
			step++;
		}
	}
