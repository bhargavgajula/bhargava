class MergeSort {
	public static void mergeSort(int[] arr, int low, int high) {
		if (low < high) {
			int mid = (low + high) / 2;
			mergesort(int[] arr, int low, int mid);
			mergesort(int[] arr, int mid+1, int high);
		}
	}
	public static void merge(int[] arr,int low,int mid, int high) {
		int[] temp = new int[arr.length];
		int i = low;
		int j = mid;
