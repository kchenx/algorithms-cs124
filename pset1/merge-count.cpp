// Merge sort algorithm to count inversions
// Solves CS 124 programming problem in directory

#include <iostream>
#include <deque>

long counter = 0;

// merge(s, t)
//    Merge algorithm for merge sort. Takes two already sorted 
//    arrays and combines into sorted array. Counts number of
//    inversions in the array.

std::deque<long> merge(std::deque<long> s, std::deque<long> t) {
    if (s.empty()) {
        return t;
    }
    else if (t.empty()) {
        return s;
    }

    long i = 0;
    long j = 0;
    long slen = s.size();
    long tlen = t.size();

    std::deque<long> u;

    // add elements in order to new array
    while (i < slen && j < tlen) {
        if (s.front() <= t.front()) {
            u.push_back(s.front());
            s.pop_front();
            i += 1;
        } else {
            j += 1;
            u.push_back(t.front());
            t.pop_front();
            // number of inversions are elements remaining in `s`
            counter += slen - i;
        }
    }

    // add remainder of `s` or `t`
    if (i < slen) {
        u.insert(u.end(), s.begin(), s.end());
    } else {
        u.insert(u.end(), t.begin(), t.end());
    }
    return u;
}


// mergesort(s)
//    Sorts an array using merge sort algorithm

std::deque<long> mergesort(std::deque<long> s) {
    if (s.empty() || s.size() <= 1) {
        return s;
    }

    // split into two subarrays and recursively sort those
    long slen = s.size();
    std::deque<long> s1(s.begin(), s.begin() + slen/2);
    std::deque<long> s2(s.begin() + slen/2, s.end());

    return merge(mergesort(s1), mergesort(s2));
}



int main() {
    // get input from user
    long N, M;
    std::cin >> N >> M;

    std::deque<long> tenacity;
    std::deque<long> major;

    long temp;
    for (long i = 0; i < N; ++i) {
        std::cin >> temp;
        tenacity.push_back(temp);
    }
    for (long i = 0; i < N; ++i) {
        std::cin >> temp;
        major.push_back(temp);
    }

    // sort tenacity longo list by major
    std::deque< std::deque<long> > people;

    for (long i = 0; i < N; ++i) {
        while (major.at(i) > people.size()) {
            std::deque<long> temp;
            people.push_back(temp);
        }
        people.at(major[i] - 1).push_back(tenacity.at(i));
    }

    // count number of inversions
    mergesort(tenacity);
    long total = counter;
    counter = 0;

    // subtract double counting inversions from people with same major
    for (long i = 0; i < people.size(); ++i) {
        mergesort(people.at(i));
        total -= counter;
        counter = 0;
    }

    std::cout << total << std::endl;
}

