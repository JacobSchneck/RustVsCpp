// Jacob Schneck
// CS 120
// Module Three: Open Ended Project

#include<chrono>
#include<fstream> 
#include<iostream> 
#include<iomanip>
#include<vector>
#include<string> 

using namespace std;
using ns = chrono::duration<int, nano>;

//========================= Declarations ========================= 

/*  read_numbers(string filename, int num_lines)
    input: filename, number of lines to read
    output: vector<int> num
*/ 
vector<int> read_numbers(string filename, int num_lines);

/*  merge_sort(vector<int> vec) 
    input: reference to a vector that will be sorted
    output: void
*/ 
vector<int> merge_sort(vector<int> &vec);
vector<int> merge(vector<int> left, vector<int> right);

/*  binary_search(vector<int> vec, num):
    input: reference to vector and number to find
    output: index (-1 if not found)
*/
int binary_search(vector<int> vec, int value);

// Testing Functions
bool test_read_numbers();
bool test_merge_sort();
bool test_binary_search();

//========================= Driver =============================== 

int main() {
    test_read_numbers();
    test_merge_sort();
    test_binary_search();

    double elapsed;
    clock_t start;    
    clock_t end; 

    string filename = "numbers.txt";
    int num_lines = 10000;
    
    string outfile = "cpp_data.txt";
    ofstream f;
    f.open(outfile);
    auto before = chrono::system_clock::now();
    vector<int> vec_nums = read_numbers(filename, num_lines);
    ns duration = chrono::system_clock::now() - before;
    f << duration.count() << endl;

    before = chrono::system_clock::now();
    vector<int> sorted_vec_nums = merge_sort(vec_nums);
    duration = chrono::system_clock::now() - before;
    f << duration.count() << endl;

    before = chrono::system_clock::now();
    int index = binary_search(sorted_vec_nums, 85430);
    duration = chrono::system_clock::now() - before;
    f << duration.count() << endl;
    f.close(); 

    return 0;
}

//======================== Definitions ===========================

// read_numbers(..)
vector<int> read_numbers(string filename, int num_lines) {
    vector<int> vec = vector<int>(num_lines);
    fstream f;
    f.open(filename);
    int num;
    for (int i = 0; i < num_lines; ++i) {
        f >> num;
        vec[i] = num;
    }
    f.close();

    return vec;
}

// merge_sort(..) 
vector<int> merge_sort(vector<int> &vec) {
    if (vec.size() <= 1) {
        return vec;
    }
    int middle = vec.size() / 2;
    vector<int> left (vec.begin(), vec.begin() + middle);
    vector<int> right(vec.begin() + middle, vec.end());

    return merge(merge_sort(left), merge_sort(right));
}

vector<int> merge(vector<int> left, vector<int> right) {
    size_t index_left = 0;
    size_t index_right = 0;
    vector<int> results;
    
    while (index_left < left.size() && index_right < right.size()) {
        if (left[index_left] < right[index_right]) {
            results.push_back(left[index_left]);
            ++index_left;
        } else {
            results.push_back(right[index_right]);
            ++index_right;
        }
    }
    
    while( index_left < left.size() ) {
        results.push_back(left[index_left]);
        ++index_left;
    }

    while( index_right < right.size() ) {
        results.push_back(right[index_right]);
        ++index_right;
    }

    return results;
}

// binary_search(..)
int binary_search(vector<int> vec, int value) {
    int mid;
    int first = 0;
    int last = vec.size() - 1;

    while (first <= last) {
        mid =  (first + last) / 2;
        if (vec[mid] == value) {
            return mid;
        } 
        // bottom half
        if (vec[mid] > value) {
            last = mid - 1;
        } else {
            first = mid + 1;
        }
    }

    // value not found
    return -1;
}

//======================== Testing ==============================

bool test_read_numbers() {
    bool passed = true;
    string filename = "numbers.txt";
    int num_lines = 10000;
    vector<int> vec_nums = read_numbers(filename, num_lines);

    if (vec_nums[0] != 26777 && vec_nums[32] != 90607 && vec_nums[300] != 5998) {
        cout << "read_numbers(..): Test One Failed" << endl;
        passed = false;
    }

    return false;
}

bool test_merge_sort() {
    vector<int> vec = {2, 1, 8, 3, 7, 4, 9, 5, 10, 6};
    vector<int> sort_vec = merge_sort(vec);

    for (int i = 0; i < sort_vec.size(); ++i) {
        if ( (i + 1) != sort_vec[i]) {
            cout << "merge_sort(..): Test One Failed" << endl;
            return false;
        }
    }
    return true;
}

bool test_binary_search() { 
    bool passed = true;

    vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int index = binary_search(vec, 4); 
    if (vec[index] != 4) {
        cout << "binary_search(..): Test One Failed" << endl;
        passed = false;
    }

    index = binary_search(vec, 6); 
    if (vec[index] != 6) {
        cout << "binary_search(..): Test Two Failed" << endl;
        passed = false;
    }

    index = binary_search(vec, 11); 
    if  (index != -1) {
        cout << "binary_search(..): Test Three Failed" << endl;
        passed = false;
    }

    return passed;
}