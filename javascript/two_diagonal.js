

// Javascript Code for Find difference between sums
// of two diagonals

function difference(arr,n)
	{
		// Initialize sums of diagonals
		let d1 = 0, d2 = 0;
	
		for (let i = 0; i < n; i++)
		{
			for (let j = 0; j < n; j++)
			{
				// finding sum of primary diagonal
				if (i == j)
					d1 += arr[i][j];
	
				// finding sum of secondary diagonal
				if (i == n - j - 1)
					d2 += arr[i][j];
			}
		}
	
		// Absolute difference of the sums
		// across the diagonals
		return Math.abs(d1 - d2);
	}
	
	/* Driver program to test above function */
	
		let n = 3;
		
		let arr =
		[
			[11, 2, 4],
			[4 , 5, 6],
			[10, 8, -12]
		];
	console.log(difference(arr, n))
