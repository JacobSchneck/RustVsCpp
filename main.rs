// Jacob Schneck
// CS 120
// Module Three: Open Ended Project

use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind, Read};

//========================= Driver =============================== 
fn main() {
    let filename: String = String::from("numbers.txt");
    let num_lines: u32 = 10;

    let vec_nums = read_numbers(filename, num_lines);
    // for n in vec_nums.iter() {
    //     println!("> {}", n);
    // }

}

//======================== Definitions ===========================

fn read_numbers(filename: String, num_lines: u32) -> Vec<u32> {
    let reader = BufReader::new(File::open(filename).expect("File not Found"));
    let mut return_vector: Vec<u32> = vec![];

    for line in reader.lines() {
        let string = line.unwrap();
        println!("{}", string);
        
        // match line {
        //     Err(why) => panic!("{:?}", why),
        //     Ok(string) => match string.trim().parse::<u32>() {
        //         None => panic!("Not a number"),
        //         Some(number)
        //     }
        // }
        // return_vector.push(line.unwrap());
    } 

    return_vector
}