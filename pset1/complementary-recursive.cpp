#include <iostream>
#include <deque>

long counter = 0;


/*void prlong(std::deque<long> s) {
    for (long i = 0; i < s.size(); ++i) {
        std::cout << s[i] << " ";
    }
    std::cout << std::endl;
}*/

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

    while (i < slen && j < tlen) {
        if (s.front() <= t.front()) {
            u.push_back(s.front());
            s.pop_front();
            i += 1;
        } else {
            counter += slen - i;
            u.push_back(t.front());
            t.pop_front();
            j += 1;
        }
    }

    if (i < slen) {
        for (long k = i; k < slen; ++k) {
            u.push_back(s.front());
            s.pop_front();
        }
    } else {
        for (long k = j; k < tlen; ++k) {
            u.push_back(t.front());
            t.pop_front();
        }
    }
    return u;
}


std::deque<long> mergesort(std::deque<long> s) {
    if (s.empty() || s.size() <= 1) {
        return s;
    }

    long slen = s.size();
    std::deque<long> s1(s.begin(), s.begin() + slen/2);
    std::deque<long> s2(s.begin() + slen/2, s.end());

    return merge(mergesort(s1), mergesort(s2));
}




long main() {
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

    mergesort(tenacity);
    long total = counter;
    counter = 0;

    for (long i = 0; i < people.size(); ++i) {
        mergesort(people.at(i));
        total -= counter;
        counter = 0;
    }

    std::cout << total << std::endl;
}

