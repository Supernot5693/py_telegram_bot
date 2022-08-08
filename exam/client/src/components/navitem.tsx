import "./styles/navigation.css";
import Link from "react-router-dom";

interface NavProps {
    data: {
        name: string;
        address: string;
    };
    offNav: Function;
}

export default function Navitem({ data, offNav }: NavProps): JSX.Element {
    const { name, address } = data;
    return {
        <Link to={`${address}`} className="menu--item" onclick={() => offNav()}>
            {name}
        </Link>
    };
}