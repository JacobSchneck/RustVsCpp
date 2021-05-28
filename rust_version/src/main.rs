// Jacob Schneck
// CS 120
// Module Three: Open Ended Project

use std::fs;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::time::{Duration, Instant};
use std::path::Path;

//========================= Driver =============================== 
fn main() {
    let filename: String = String::from("numbers.txt");
    let num_lines: usize = 10000;

    let path = Path::new("rust_data.txt");

    let mut start = Instant::now();
    let vec_nums = read_numbers(filename, num_lines);
    let mut duration = start.elapsed();
    let data1 = duration.as_nanos();
    
    
    start = Instant::now();
    let sorted_vec_nums = merge_sort(&vec_nums);
    duration = start.elapsed();
    let data2 = duration.as_nanos();

    start = Instant::now();
    let index = binary_search(&sorted_vec_nums, 85430).ok(); // returns only result ok, otherwise none
    duration = start.elapsed();
    let data3 = duration.as_nanos();

    let text = format!("{}\n{}\n{}\n", data1, data2, data3);
    fs::write(path, text).expect("Unable to write file");
}

//======================== Definitions ===========================

fn read_numbers(filename: String, num_lines: usize) -> Vec<i32> {
    let reader = BufReader::new(File::open(filename).expect("File not Found"));
    let mut return_vector: Vec<i32> = vec![];

    let mut string: String;
    for line in reader.lines() {
        string = line.unwrap();
        return_vector.push(string.parse::<i32>().unwrap());
    } 

    return_vector[0..num_lines].to_vec()
}

fn merge_sort(vec: &Vec<i32>) -> Vec<i32> {
    if vec.len() <= 1 {
        vec.to_vec()
    } else { // not sure why else statement was needed but it was 

        let mid = vec.len() / 2;
        let left = merge_sort(&vec[..mid].to_vec());
        let right = merge_sort(&vec[mid..].to_vec());

        merge(&left, &right)
    }

}

fn merge(left: &Vec<i32>, right: &Vec<i32>) -> Vec<i32> {
    let mut i_left = 0;
    let mut i_right = 0;
    let mut result = vec![];

    while i_left < left.len() && i_right < right.len() {
        if left[i_left] < right[i_right] {
            result.push(left[i_left]);
            i_left += 1;
        } else {
            result.push(right[i_right]);
            i_right += 1;
        }
    }

    while i_left < left.len() {
        result.push(left[i_left]);
        i_left += 1;
    }

    while i_right < right.len() {
        result.push(right[i_right]);
        i_right += 1;
    }

    result
}

fn binary_search(vec: &Vec<i32>, value: i32) -> Result<usize, i32> {
    let mut mid;
    let mut first: usize = 0;
    let mut last: usize = vec.len() - 1;
    while first <= last {
        mid = (first + last) / 2;
        if vec[mid] == value {
            return Ok(mid)
        } else if vec[mid] > value {
            last = mid - 1;
        } else {    
            first = mid + 1;
        }
    }
    // Value not found 
    Err(-1)
}